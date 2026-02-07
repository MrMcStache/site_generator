import unittest
from markdown_to_html_node import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_list(self):
        md = """
# This is a heading1

- This is **bolded** item in the list
- Second item
- Third _italic_ item
"""

        md2 = """
##### This is a heading5

1. This is **bolded** item in the list
2. Second item
3. Third _italic_ item
"""

        node = markdown_to_html_node(md)
        node2 = markdown_to_html_node(md2)
        html = node.to_html()
        html2 = node2.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading1</h1><ul><li>This is <b>bolded</b> item in the list</li><li>Second item</li><li>Third <i>italic</i> item</li></ul></div>",
        )
        self.assertEqual(
            html2,
            "<div><h5>This is a heading5</h5><ol><li>This is <b>bolded</b> item in the list</li><li>Second item</li><li>Third <i>italic</i> item</li></ol></div>"
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
>This is a **bold** quote
>But this isn't
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a <b>bold</b> quote But this isn't</blockquote></div>",
        )

    def test_mixed_blocks(self):
        md = """
# Title

This is a **bold** paragraph

- Item one
- Item _two_

```
code line 1
code line 2
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title</h1><p>This is a <b>bold</b> paragraph</p><ul><li>Item one</li><li>Item <i>two</i></li></ul><pre><code>code line 1\ncode line 2\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
