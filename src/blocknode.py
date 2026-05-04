from enum import Enum
import re
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType
from function_helper import markdown_to_blocks, text_to_textnodes

class BlockType(Enum):
    PAR = "paragraph"
    HEAD = "heading"
    QUOTE = "quote"
    CODE = "code"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def block_to_block_type(block : str) -> BlockType:
    heading_prefix = [(i * "#")+" " for i in range(1, 7)]
    for sw in heading_prefix:
        if block.startswith(sw):
            return BlockType.HEAD
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        return BlockType.QUOTE
    
    if block.startswith("- "):
        return BlockType.U_LIST
    
    if re.findall(r"^[0-9]*\. ", block):
        return BlockType.O_LIST
    
    return BlockType.PAR

def markdown_to_html_node(markdown : str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    childern = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            childern.append(
                ParentNode(
                    "pre",
                    [LeafNode("code", block.strip("```").strip()+"\n")]
                )
            )
            continue

        if block_type == block_type.HEAD:
            childern.append(
                LeafNode(
                    f"h{block.count("#")}",
                    process_inline(block.strip("# "))
                )
            )
            continue
        
        if block_type == BlockType.QUOTE:
            childern.append(
                LeafNode("blockquote", process_inline(block.replace(">", "")))
            )

            continue
        
        if block_type == BlockType.U_LIST:
            childern.append(
                ParentNode(
                    "ul",
                    [
                        LeafNode(
                            "li",
                            process_inline(val.strip())
                        )
                        for val in block.split("- ")
                        if val != ""
                    ]
                )
            )

            continue

        if block_type == BlockType.O_LIST:
            childern.append(
                ParentNode(
                    "ol",
                    [
                        LeafNode(
                            "li",
                            process_inline(val)
                        )
                        for val in [
                            item.split(". ", 1)[1]
                            for item in block.split("\n")
                        ]
                    ]
                )
            )

            continue
        
        if block != "":
            childern.append(LeafNode('p',process_inline(block)))
    
    return ParentNode('div', childern)

def process_inline(block):
    block = block.strip().replace("\n"," ")
    inline_str = ""
    for node in text_to_textnodes(block):
        if node.text_type == TextType.TEXT:
            inline_str += node.text
            continue
        if node.text_type == TextType.BOLD:
            inline_str += f"<b>{node.text}</b>"
            continue
        if node.text_type == TextType.CODE:
            inline_str += f"<code>{node.text}</code>"
            continue
        if node.text_type == TextType.ITALIC:
            inline_str += f"<i>{node.text}</i>"
            continue
        if node.text_type == TextType.IMAGE:
            inline_str += f"<img src=\"{node.url}\" alt=\"{node.text}\">"
            continue
        if node.text_type == TextType.LINK:
            inline_str += f"<a href=\"{node.url}\">{node.text}</a>"
            continue
    return inline_str
