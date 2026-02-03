from enum import Enum

class TextTypes(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        if isinstance(text_type, TextTypes):
            self.text_type = text_type
        else:
            raise Exception(f"ERROR: {text_type} is not a valid text type")
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
