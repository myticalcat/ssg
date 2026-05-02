import unittest

from function_helper import text_node_to_html_node, split_nodes_delimiter

from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestText2HTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    

    def test_text2html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        true_html = LeafNode(None, "This is a text node")
        self.assertEqual(html_node.to_html(), true_html.to_html())


    def test_text2html_img(self):
        node = TextNode("cat image", TextType.IMAGE, "cat.jpg")
        html_node = text_node_to_html_node(node)
        true_html = LeafNode("img", "", {
            "src":"cat.jpg",
            "alt":"cat image"
        })
        self.assertEqual(html_node.to_html(), true_html.to_html())
    

    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes
        )

    def test_delimiter_end(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
            new_nodes
        )

    def test_delimiter_end_incomplete(self):
        node = TextNode("This is text with a `code block", TextType.TEXT)

        self.assertRaises(
            ValueError,
            split_nodes_delimiter,
            [node], "`", TextType.CODE
        )

    def test_delimiter_slash(self):
        node = TextNode("This is text with a \\code block\\ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "\\", TextType.BOLD)

        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()