from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

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