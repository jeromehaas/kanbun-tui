from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.reactive import reactive
from app.widgets.TaskWidget import TaskWidget

# CLASS: LANE WIDGET
class LaneWidget(Container):

    # DEFINE LANE
    lane = reactive(None)

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHOW MESSAGE IF NO LANE IS AVAILABLE
        if self.lane is None:
            yield Label("No Lane")
            return

        # PRINT LABEL FOR LANE
        yield Label(self.lane.name)

        # LOOP OVER TASKS
        for task in self.lane.tasks:

            # GET TASKS WIDGET AND ASSIGN TASKS TO IT
            task_widget = TaskWidget()
            task_widget.task = task

            # DISPLAY TASKS WIDGET
            yield task_widget

