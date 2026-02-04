import unittest
from split_nodes_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
        node3 = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        new_nodes3 = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        new_nodes4 = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        new_nodes5 = split_nodes_delimiter([node3], "_", TextType.ITALIC)
        new_nodes6 = split_nodes_delimiter([node, node2, node3], "_", TextType.ITALIC)

        self.assertEqual(str(new_nodes), "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]")
        self.assertEqual(str(new_nodes2), "[TextNode(This is text with a , text, None), TextNode(bold, bold, None), TextNode( word, text, None)]")
        self.assertEqual(str(new_nodes3), "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None), TextNode(This is text with a **bold** word, text, None)]")
        self.assertEqual(str(new_nodes4), "[TextNode(This is text with a `code block` word, text, None), TextNode(This is text with a , text, None), TextNode(bold, bold, None), TextNode( word, text, None)]")
        self.assertEqual(str(new_nodes5), "[TextNode(This is text with an , text, None), TextNode(italic, italic, None), TextNode( word, text, None)]")
        self.assertEqual(str(new_nodes6), "[TextNode(This is text with a `code block` word, text, None), TextNode(This is text with a **bold** word, text, None), TextNode(This is text with an , text, None), TextNode(italic, italic, None), TextNode( word, text, None)]")

    def test_errors(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold* word", TextType.TEXT)
        node3 = TextNode("This is text with an _italic word", TextType.TEXT)

        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "`", TextType.CODE))
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node2], "**", TextType.BOLD))
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node3], "_", TextType.ITALIC))


if __name__ == "__main__":
    unittest.main()
