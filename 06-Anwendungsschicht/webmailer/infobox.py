INFO = "tucbox-tip-info"
SUCCESS = "tucbox-tip"
WARNING = "tucbox-tip-warning"
ERROR = "tucbox-tip-danger"


class Infobox:
    def __init__(self, type, body):
        self.type = type
        self.body = body

    def render(self):
        return f"<div class='{self.type}'>{self.body}</div>"
