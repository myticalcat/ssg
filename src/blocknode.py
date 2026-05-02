from enum import Enum
import re
from htmlnode import HTMLNode, ParentNode, LeafNode
from function_helper import markdown_to_blocks

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
                    LeafNode("code", block.strip("```"))
                )
            )
            continue

        if block_type == block_type.HEAD:
            childern.append(
                LeafNode(
                    f"h{block.count("#")}",
                    block.strip("# ")
                )
            )
            continue
        
        if block_type == BlockType.QUOTE:
            childern.append(
                LeafNode("blockquote", block.replace(">", ""))
            )

            continue
        
        if block_type == BlockType.U_LIST:
            childern.append(
                ParentNode(
                    "ul",
                    [
                        LeafNode(
                            "li",
                            val
                        )
                        for val in block.split("- ")
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
                            val
                        )
                        for val in [
                            item.strip(". ")
                            for item in block.split("\n")
                        ]
                    ]
                )
            )

            continue

        childern.append(LeafNode('p',))
    
    return ParentNode('div', childern)