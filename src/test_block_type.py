import unittest
from block_type import *

class TestBlockType(unittest.TestCase):
    def test_blocks(self):
        block = "### Heading text"
        block2 = "```\nCode text\n```"
        block3 = "Paragraph text"
        block4 = ">Quote\n> Block"
        block5 = "- Unordered\n- List\n- Text"
        block6 = "1. Ordered\n2. List\n3. Text"
        block7 = "1. Ordered\n2. List\n4. Text"
        block8 = "- Unordered\n- List\n Text"
        block9 = ">Quote\n Block"
        block10 = "```\nCode text\n``"

        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.CODE)
        self.assertEqual(block_to_block_type(block3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(block4), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(block5), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block6), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(block7), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(block8), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type(block9), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type(block10), BlockType.CODE)

if __name__ == "__main__":
    unittest.main()
