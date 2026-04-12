from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container, HorizontalScroll
from textual.reactive import reactive

from app.widgets.LaneWidget import LaneWidget

# LANES CONTAINER WIDGET CLASS
class LanesContainerWidget(HorizontalScroll):

    lanes = reactive([], recompose=True)

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
        yield Label("Lanes")

        if not self.lanes:
            yield Label("No Lanes")
            return

        for lane in self.lanes:
            yield LaneWidget(lane)