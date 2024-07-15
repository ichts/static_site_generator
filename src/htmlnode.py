class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""

        props_html = ''
        for k, v in self.props.items():
            props_html += f' {k}="{v}"'

        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, props=None, tag=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag is None:
            return f"{self.value}"

        html_string = f"<{self.tag}{self.props_to_html()}>{
            self.value}</{self.tag}>"

        return html_string

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag!")

        if self.children is None:
            raise ValueError("ParentNode must have at least a  child!")

        children_html = ''

        for child in self.children:
            children_html += f'{child.to_html()}'

        parent_html = f'<{self.tag}{self.props_to_html()}>{children_html}{
            self.value}</{self.tag}>'

        return parent_html

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
