from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container, VerticalScroll
from app.widgets.TaskWidget import TaskWidget


# LANE WIDGET CLASS
class LaneWidget(VerticalScroll):

    # BUILD WIDGET
    def compose(self)-> ComposeResult:
        yield Label("LaneA")
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


