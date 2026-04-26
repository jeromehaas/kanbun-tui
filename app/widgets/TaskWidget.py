from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.reactive import reactive
from app.models.Task import Task

# CLASS: TASK WIDGET
class TaskWidget(Container):
    MAXIMUM_NUMBER_OF_DIGITS = 25

    # DEFINE TASKS
    task = reactive(None)

    def __init__(self, task: Task):
        super().__init__()
        self.task = task

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHOW MESSAGE IF NO TASKS ARE AVAILABLE
        if self.task is None:
            yield Label("No Tasks")
            return

        # SHORTEN TITLE IF TO LONG
        if len(self.task.title) > self.MAXIMUM_NUMBER_OF_DIGITS:
            title = str(self.task.title[:self.MAXIMUM_NUMBER_OF_DIGITS]) + "..."
        else:
            title = str(self.task.title)

        # SHORTEN DESCRIPTION IF TO LONG
        if len(self.task.description) > self.MAXIMUM_NUMBER_OF_DIGITS:
            description = str(self.task.description[:self.MAXIMUM_NUMBER_OF_DIGITS]) + "..."
        else:
            description = str(self.task.description)

        # DISPLAY WIDGET
        with Container():
            yield Label(f"⚬ {title}", id="title")
            yield Label(f'  {description}', id="description")
