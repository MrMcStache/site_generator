import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def testEq(self):
        node = LeafNode("a", "Lorem Ipsum", {"href": "url"})
        node2 = LeafNode("a", "Lorem Ipsum", {"href": "url"})
        node3 = LeafNode("a", "Lorem Ipsum")
        node4 = LeafNode("a", "Lorem Ipsum")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)

    def testIneq(self):
        node = LeafNode("a", "Lorem Ipsum", {"href": "https"})
        node2 = LeafNode("a", "Lorem Ipsum", {"href": "http"})
        node3 = LeafNode("a", "Ipsum Lorem", {"href": "https"})
        node4 = LeafNode("p", "Lorem Ipsum", {"href": "https"})
        node5 = LeafNode("a", "Lorem Ipsum")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

    def testError(self):
        node = LeafNode("a", None, {"href": "https://www.github.com"})
        self.assertRaises(ValueError, lambda: node.to_html())

if __name__ == "__main__":
    unittest.main()
