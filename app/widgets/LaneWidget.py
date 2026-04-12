from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container, VerticalScroll
from app.widgets.TaskWidget import TaskWidget


# LANE WIDGET CLASS
class LaneWidget(VerticalScroll):

    def __init__(self, lane):
        super().__init__()
        self.lane = lane

    # BUILD WIDGET
    def compose(self)-> ComposeResult:
        yield Label(self.lane.name)
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()
        yield TaskWidget()


