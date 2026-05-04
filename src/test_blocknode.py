import unittest

from blocknode import BlockType, block_to_block_type, markdown_to_html_node


class TestBlockNode(unittest.TestCase):
    def test_par(self):
        self.assertEqual(
            block_to_block_type("normal"),
            BlockType.PAR
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> normal"),
            BlockType.QUOTE
        )

    def test_quote_no_space(self):
        self.assertEqual(
            block_to_block_type(">normal"),
            BlockType.QUOTE
        )

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# normal"),
            BlockType.HEAD
        )

    def test_not_head(self):
        self.assertNotEqual(
            block_to_block_type("#normal"),
            BlockType.HEAD
        )


    def test_ul(self):
        self.assertEqual(
            block_to_block_type("- normal"),
            BlockType.U_LIST
        )

    def test_not_ul(self):
        self.assertNotEqual(
            block_to_block_type("-normal"),
            BlockType.U_LIST
        )

    def test_ol(self):
        self.assertEqual(
            block_to_block_type("1. normal"),
            BlockType.O_LIST
        )

    def test_not_ol(self):
        self.assertNotEqual(
            block_to_block_type("1.normal"),
            BlockType.O_LIST
        )

    def test_ol_not_starting(self):
        self.assertEqual(
            block_to_block_type("2. normal"),
            BlockType.O_LIST
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            str(html),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ul_html(self):
        md = """- 1
- 2
- 3
- 4"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>1</li><li>2</li><li>3</li><li>4</li></ul></div>",
        )

    def test_ol_html(self):
        md = """1. 1
2. 2
3. 3
4. 4"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>1</li><li>2</li><li>3</li><li>4</li></ol></div>",
        )

    def test_ol_with_dot(self):
        md = """1. 1.1.1
2. 2
3. 3
4. 4"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>1.1.1</li><li>2</li><li>3</li><li>4</li></ol></div>",
        )
if __name__ == "__main__":
    unittest.main()