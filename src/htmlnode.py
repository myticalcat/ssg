class HTMLNode():
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag : str = tag
        self.value : str = value
        self.children : list[HTMLNode] = children
        self.props : dict = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        html_str = ""

        if self.props is None:
            return html_str
        for k, v in self.props.items():
            html_str += f' {k}="{v}"'
            
        return html_str
    
    def __repr__(self):
        return {
            "tag" : self.tag,
            "value" : self.value,
            "childern" : self.children,
            "props" : self.props
        }.__repr__()


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props = None):
        super().__init__(
            tag=tag,
            value=value,
            children=None,
            props=props
        )

    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return {
            "tag" : self.tag,
            "value" : self.value,
            "props" : self.props
        }.__repr__()