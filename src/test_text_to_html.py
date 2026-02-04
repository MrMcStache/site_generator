import unittest
from text_to_html import *

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        node3 = TextNode("This is an italic node", TextType.ITALIC)
        node4 = TextNode("This is a code node", TextType.CODE)
        node5 = TextNode("This is a link node", TextType.LINK, "https://")
        node6 = TextNode("This is an image node", TextType.IMAGE, "src/img.jpg")

        html_node = text_node_to_html_node(node)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)
        html_node4 = text_node_to_html_node(node4)
        html_node5 = text_node_to_html_node(node5)
        html_node6 = text_node_to_html_node(node6)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a bold node")

        self.assertEqual(html_node3.tag, "i")
        self.assertEqual(html_node3.value, "This is an italic node")

        self.assertEqual(html_node4.tag, "code")
        self.assertEqual(html_node4.value, "This is a code node")

        self.assertEqual(html_node5.tag, "a")
        self.assertEqual(html_node5.value, "This is a link node")
        self.assertEqual(html_node5.props, {"href": "https://"})

        self.assertEqual(html_node6.tag, "img")
        self.assertEqual(html_node6.value, "")
        self.assertEqual(html_node6.props, {"src": "src/img.jpg", "alt": "This is an image node"})

if __name__ == "__main__":
    unittest.main()
