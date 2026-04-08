from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

class BoardsContainer(Container):
    CSS_PATH="../styles/widgets/boards-container.tcss"


    def compose(self) -> ComposeResult:
        yield Label("Boards")

