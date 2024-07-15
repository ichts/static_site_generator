from textnode import *
from htmlnode import LeafNode


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
