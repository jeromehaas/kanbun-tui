from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.reactive import reactive

# CLASS: TASK WIDGET
class TaskWidget(Container):

    # DEFINE TASKS
    task = reactive(None)

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHOW MESSAGE IF NO TASKS ARE AVAILABLE
        if self.task is None:
            yield Label("No Task")
            return

        # DISPLAY LABEL
        yield Label(self.task["title"])