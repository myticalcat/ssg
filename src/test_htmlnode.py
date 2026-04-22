import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq_props2html(self):
        v1 = HTMLNode(props=   {
            "href": "https://www.google.com",
            "target": "_blank",
        }).props_to_html() 
        v2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(v1,v2)

    def test_eq_repr(self):
        node =HTMLNode(props=   {
            "href": "https://www.google.com",
            "target": "_blank",
        }).__repr__()
        node2 =HTMLNode(props=   {
            "href": "https://www.google.com",
            "target": "_blank",
        }).__repr__()
        
        self.assertEqual(node, node2)

    def test_neq(self):
        node =HTMLNode(props=   {
            "href": "https://www.google.com",
            "target": "_blank",
        }).__repr__()
        node2 =HTMLNode(props=   {
            "href": "https://www.google.com",
            "target": "not_blank",
        }).__repr__()
        
        self.assertNotEqual(node, node2)

    def test_props_none(self): 
        self.assertEqual(HTMLNode(props=None).props_to_html(), "")


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {
            "href" : "mytical.cat"
        })
        self.assertEqual(node.to_html(), '<a href="mytical.cat">Hello, world!</a>')

    def test_leaf_to_html_no_value(self):
        invalid = LeafNode("p", None, {"a":"cat.com"})
        self.assertRaises(ValueError, invalid.to_html)

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()