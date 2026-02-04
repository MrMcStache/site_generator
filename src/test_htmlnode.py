import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def testEq(self):
        node = HTMLNode("<p>", "Lorem Ipsum", None, None)
        node2 = HTMLNode("<p>", "Lorem Ipsum", None, None)
        self.assertEqual(node, node2)

    def testIneq(self):
        node = HTMLNode("<p>", "Lorem Ipsum", None, None)
        node2 = HTMLNode("<p>", "Lorem Ipsum", None, {"href": "https://www.github.com"})
        node3 = HTMLNode("<p>", "Lorem Ipsum", "<h1>", None)
        node4 = HTMLNode("<p>", "Ipsum Lorem", None, None)
        node5 = HTMLNode("<h1>", "Lorem Ipsum", None, None)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

if __name__ == "__main__":
    unittest.main()
