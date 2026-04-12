from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container, HorizontalScroll

from app.widgets.LaneWidget import LaneWidget

# LANES CONTAINER WIDGET CLASS
class LanesContainerWidget(HorizontalScroll):

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
        yield Label("Lanes")
        yield LaneWidget()
        yield LaneWidget()
        yield LaneWidget()
