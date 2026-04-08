from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

# LANES CONTAINER CLASS
class LanesContainer(Container):
    CSS_PATH="../styles/widgets/lanes-container.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Lanes")
