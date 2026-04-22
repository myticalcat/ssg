from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"


class TextNode():
    
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and other.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"