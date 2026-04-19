from textual.app import ComposeResult
from textual.message import Message
from textual.events import Click
from textual.widgets import Label, ListView,ListItem
from textual.containers import Container
from textual.reactive import reactive
from app.widgets.TaskWidget import TaskWidget

# CLASS: LANE WIDGET
class LaneWidget(Container):

    # DEFINE LANE
    lane = reactive(None)

    class LaneSelected(Message):

        # METHOD: INIT
        def __init__(self, lane):

            # EXTEND CLASS
            super().__init__()

            # SETUP FIELDS
            self.lane = lane

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

    def post_lane_selected(self) -> None:

        # POST SELECTED LANE IF AVAILABLE
        if self.lane is not None:
            self.post_message(self.LaneSelected(self.lane))
            self.notify(f"Lane Message Posted: {self.lane.name}")

    def on_click(self, event: Click) -> None:

        # DISPATCH SELECTED LANE ON CLICK
        self.post_lane_selected()
        self.notify("Click")

    def on_focus(self) -> None:

        # DISPATCH SELECTED LANE WHEN WIDGET IS FOCUSED
        self.post_lane_selected()
        self.notify("Focus")

    def on_list_view_selected(self, event: ListView.Selected) -> None:

        # GET SELECTED ITEM
        selected_item = event.item


        # GET TASK
        task_widget = selected_item.query_one(TaskWidget)
        task_id = task_widget.task["id"]


        # DEBUG
        self.notify(f"Selected task: ID{str(task_id)}")


        # DISPATCH SELECTED TASK
        self.post_message(self.TaskSelected(task_id))
