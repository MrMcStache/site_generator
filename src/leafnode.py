from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            if (
                self.tag == other.tag and self.value == other.value and
                self.children == other.children and self.props == other.props
            ):
                return True
            return False

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError(f"ERROR: leaf node has no value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
