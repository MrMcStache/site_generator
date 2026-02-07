import unittest
from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_titles(self):
        md = """
# This is a heading 1

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

### This is a heading 3

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        md2 = """
##### This is a heading 5

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

# This is a heading 1

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        md3 = """
#### This is a heading 4

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

## This is a heading 2

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        title = extract_title(md)
        title2 = extract_title(md2)

        self.assertEqual(title, "This is a heading 1")
        self.assertEqual(title2, "This is a heading 1")
        self.assertRaises(Exception, lambda: extract_title(md3))

if __name__ == "__main__":
    unittest.main()
