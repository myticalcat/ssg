import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()


 