import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        c_node = LeafNode("i", "italic")
        c_node2 = LeafNode("img", "image", {"src": "src/image.jpg", "alt": "altText"})

        #main cases
        p_node = ParentNode("div", [c_node])
        props_node = ParentNode("div", [c_node], {"title": "titleText"})

        #equal
        p_node2 = ParentNode("div", [c_node])

        #not equal
        p_node3 = ParentNode("div", [c_node], {"title": "titleText"})
        p_node4 = ParentNode("div", [c_node2])
        p_node5 = ParentNode("p", [c_node])
        props_node2 = ParentNode("div", [c_node], {"title": "titleText", "alt": "altText"})

        self.assertEqual(p_node, p_node2)
        self.assertEqual(props_node, p_node3)

        self.assertNotEqual(p_node, p_node3)
        self.assertNotEqual(p_node, p_node4)
        self.assertNotEqual(p_node, p_node5)
        self.assertNotEqual(p_node, props_node2)
        self.assertNotEqual(props_node, props_node2)

    def test_error(self):
        c_node = LeafNode("i", "italic")

        p_node = ParentNode("", [c_node])
        p_node2 = ParentNode(None, [c_node])
        p_node3 = ParentNode("div", [])
        p_node4 = ParentNode("div", None)

        self.assertRaises(ValueError, lambda: p_node.to_html())
        self.assertRaises(ValueError, lambda: p_node2.to_html())
        self.assertRaises(ValueError, lambda: p_node3.to_html())
        self.assertRaises(ValueError, lambda: p_node4.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")
if __name__ == "__main__":
    unittest.main()
