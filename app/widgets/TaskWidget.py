from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.reactive import reactive
from app.models.Task import Task

# CLASS: TASK WIDGET
class TaskWidget(Container):

    # DEFINE TASKS
    task = reactive(None)

    def __init__(self, task: Task):
        super().__init__()
        self.task = task

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHOW MESSAGE IF NO TASKS ARE AVAILABLE
        if self.task is None:
            yield Label("No Task")
            return

        # DISPLAY LABEL
        yield Label(self.task.title)
