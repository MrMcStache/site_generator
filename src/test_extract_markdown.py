import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text3 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        matches = extract_markdown_images(text)
        matches2 = extract_markdown_images(text2)
        #matches3 = extract_markdown_images(text3)
        #print(matches2)

        self.assertEqual(str(matches), "[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]")
        self.assertEqual(str(matches2), "[('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]")
        #self.assertEqual(str(matches3), "")

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text3 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        matches = extract_markdown_links(text)
        matches2 = extract_markdown_links(text2)
        #matches3 = extract_markdown_links(text3)
        #print(matches3)

        self.assertEqual(str(matches), "[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]")
        self.assertEqual(str(matches2), "[('to boot dev', 'https://www.boot.dev')]")
        #self.assertEqual(str(matches2), "")

if __name__ == "__main__":
    unittest.main()
