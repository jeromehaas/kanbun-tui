from textual.app import ComposeResult
from textual.message import Message
from textual.widgets import Label, ListView,ListItem
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

        with ListView():
            # LOOP OVER TASKS
            for task in self.lane.tasks:
                yield ListItem(TaskWidget(task))

    class TaskSelected(Message):

        # METHOD: INIT
        def __init__(self, task_id):

            # EXTEND CLASS
            super().__init__()

            # SETUP FIELDS
            self.task = task_id
    def on_list_view_selected(self, event: ListView.Selected) -> None:

        # GET SELECTED ITEM
        selected_item = event.item

        # GET BOARD TILE and BOARD
        task_widget = selected_item.query_one(TaskWidget)
        task_id = task_widget.id

        # DISPATCH SELECTED BOARD
        self.post_message(self.TaskSelected(task_id))