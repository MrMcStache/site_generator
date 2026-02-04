import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.github.com")
        node4 = TextNode("This is a text node", TextType.BOLD, "https://www.github.com")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)

    def test_ineq(self):
        node = TextNode("Test Node", TextType.ITALIC, "https://www.github.com")
        node2 = TextNode("Test Node", TextType.ITALIC)
        node3 = TextNode("Test node", TextType.ITALIC, "https://www.github.com")
        node4 = TextNode("Test Node", TextType.BOLD, "https://www.github.com")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)

    def test_error(self):
        self.assertRaises(AttributeError, lambda: TextNode("This is a text node", TextType.SUPER))

if __name__ == "__main__":
    unittest.main()
