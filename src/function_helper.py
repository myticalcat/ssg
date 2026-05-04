from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
import re

def text_node_to_html_node(text_node : TextNode) -> HTMLNode:
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {
            "href":text_node.url
        })
    
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img","", {
            "src":text_node.url,
            "alt":text_node.text
        } )

    return TypeError


def split_nodes_delimiter(old_nodes : list, delimiter : str, text_type : TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        partitions = node.text.split(delimiter,)
        is_text = True
        for part in partitions:
            if part == "" and is_text:
                is_text = False
                continue

            if is_text:
                new_nodes.append(TextNode(part, TextType.TEXT))
                is_text = False
                continue

            new_nodes.append(TextNode(part, text_type))
            is_text = True
        if is_text:
            raise ValueError(f"No closing delimited for {node.text}")
    return new_nodes


def extract_markdown_images(text: str):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text: str):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def split_nodes_link(nodes):
    new_nodes = []
    for n in nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        node : TextNode = n
        text = node.text
        links = extract_markdown_links(text)
        if (not links) and (text != ""):
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue
        for i, link in enumerate(links):
            splitted = text.split(f"[{link[0]}]({link[1]})", 1)
            if splitted[0] != "":
                new_nodes.append(TextNode(splitted[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if splitted[1] != "":
                text = splitted[1]
                if i == (len(links) - 1):
                    new_nodes.append(TextNode(splitted[1], TextType.TEXT))
    return new_nodes

def split_nodes_image(nodes):
    new_nodes = []
    for n in nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        node : TextNode = n
        text = node.text
        links = extract_markdown_images(text)
        if (not links) and (text != ""):
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue
        for i, link in enumerate(links):
            splitted = text.split(f"![{link[0]}]({link[1]})", 1)
            if splitted[0] != "":
                new_nodes.append(TextNode(splitted[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.IMAGE, link[1]))
            if splitted[1] != "":
                text = splitted[1]
                if i == (len(links) - 1):
                    new_nodes.append(TextNode(splitted[1], TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = split_nodes_image([TextNode(text, TextType.TEXT)])
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    return new_nodes

def markdown_to_blocks(markdown):
    return [s.strip() for s in markdown.split("\n\n")]

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No H1 header!")