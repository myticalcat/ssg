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

        for k, v in self.props.items:
            html_str += f'{k}="{v}"'
            
        return html_str
    
    def __repr__(self):
        return {
            "tag" : self.tag,
            "value" : self.value,
            "childern" : self.children,
            "props" : self.props
        }.__repr__()

