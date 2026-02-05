import unittest
from text_to_textnodes import *

class TestTextToTextnode(unittest.TestCase):
    def test_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(str(text_to_textnodes(text)), '[TextNode(This is , text, None), TextNode(text, bold, None), TextNode( with an , text, None), TextNode(italic, italic, None), TextNode( word and a , text, None), TextNode(code block, code, None), TextNode( and an , text, None), TextNode(obi wan image, image, https://i.imgur.com/fJRm4Vk.jpeg), TextNode( and a , text, None), TextNode(link, link, https://boot.dev)]')

if __name__ == "__main__":
    unittest.main()
