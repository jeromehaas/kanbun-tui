from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container


# TASK WIDGET CLASS
class TaskWidget(Container):

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
        yield Label("A Task")