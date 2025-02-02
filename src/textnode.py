from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

text_types = [text_type_text, text_type_bold, text_type_italic,
              text_type_code, text_type_link, text_type_image]


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.type not in text_types:
        raise Exception(f"Invalide text type:{text_node.text_type}")

    if text_node.type == text_type_text:
        return LeafNode(text_node.text)
    if text_node.type == text_type_bold:
        return LeafNode(text_node.text, None, "b")
    if text_node.type == text_type_italic:
        return LeafNode(text_node.text, None, "i")
    if text_node.type == text_type_code:
        return LeafNode(text_node.text, None, "code")
    if text_node.type == text_type_link:
        return LeafNode(text_node.text, {"href": text_node.url}, "a")
    if text_node.type == text_type_image:
        return LeafNode(
            '', {"src": text_node.url, "alt": text_node.text}, "img")
