import unittest

from function_helper import text_node_to_html_node

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


if __name__ == "__main__":
    unittest.main()