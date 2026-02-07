from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError("ERROR: parentnode has no tag")

        if self.children == None:
            raise ValueError("ERROR: parentnode has no children")

        html_str = f'<{self.tag}>'

        for child in self.children:
            html_str = html_str + child.to_html()

        html_str = html_str + f'</{self.tag}>'

        return html_str
