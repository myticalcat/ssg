import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.LINK, "mytical.cat")
        node2 = TextNode("This is a text node", TextType.LINK, "mytical.cat")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK, "SOMETHING.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()