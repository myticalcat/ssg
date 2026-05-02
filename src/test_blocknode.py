import unittest

from blocknode import BlockType, block_to_block_type


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

if __name__ == "__main__":
    unittest.main()