import unittest
from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
    #split_nodes_delimiter tests
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

        #print(new_nodes)

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

    #split_nodes_link tests
    def test_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(str(new_nodes), '[TextNode(This is text with a link , text, None), TextNode(to boot dev, link, https://www.boot.dev), TextNode( and , text, None), TextNode(to youtube, link, https://www.youtube.com/@bootdotdev)]')

    def test_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertEqual(str(new_nodes), '[TextNode(This is text with an , text, None), TextNode(image, image, https://i.imgur.com/zjjcJKZ.png), TextNode( and another , text, None), TextNode(second image, image, https://i.imgur.com/3elNhQu.png)]')

if __name__ == "__main__":
    unittest.main()
