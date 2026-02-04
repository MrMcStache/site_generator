class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
                return True
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""

        if self.props is None or len(self.props) == 0:
            return props_str

        for p in self.props:
            props_str = props_str + f"{p}={self.props[p]} "

        return props_str
