# IMPORTS
from textual.app import ComposeResult
from textual.message import Message
from textual.events import Click, Focus, DescendantFocus
from textual.widgets import Label, ListView,ListItem
from textual.containers import Container
from textual.reactive import reactive
from app.widgets.TaskWidget import TaskWidget
from app.models.Lane import Lane
from app.models.Task import Task

# CLASS: LANE WIDGET
class LaneWidget(Container):

    can_focus = True

    # DEFINE LANE
    lane = reactive(None)
    selected_task_id = reactive(None)

    # CLASS: LANE SELECTED
    class LaneSelected(Message):

        # METHOD: INIT
        def __init__(self, lane: Lane):

            # EXTEND CLASS
            super().__init__()

            # SETUP FIELDS
            self.lane = lane

    # CLASS: TASKS SELECTED
    class TaskSelected(Message):

        # METHOD: INIT
        def __init__(self, task: Task):

            # EXTEND CLASS
            super().__init__()

            # SETUP FIELDS
            self.task = task

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHOW MESSAGE IF NO LANE IS AVAILABLE
        if self.lane is None:
            yield Label("No Lane")
            return

        # PRINT LABEL FOR LANE
        yield Label(self.lane.name, id="label_title")

        # GET SELECTED INDEX
        selected_index = next(
            (index for index, task in enumerate(self.lane.tasks) if task.id == self.selected_task_id),
            None,
        )

        # WRAP LIST VIEW
        with ListView(initial_index=selected_index):

            # LOOP OVER TASKS
            for task in self.lane.tasks:
                yield ListItem(TaskWidget(task))

    # METHOD: POST LANE
    def post_lane_selected(self) -> None:

        # POST SELECTED LANE IF AVAILABLE
        if self.lane is not None:
            self.post_message(self.LaneSelected(self.lane))

    # LISTENER: ON CLICK
    def on_click(self, event: Click) -> None:

        # DISPATCH SELECTED LANE ON CLICK
        self.post_lane_selected()


    # LISTENER: ON FOCUS
    def on_focus(self, event: Focus) -> None:

        # DISPATCH SELECTED LANE WHEN WIDGET IS FOCUSED
        self.post_lane_selected()


    # LISTENER: ON DESCENDANT FOCUS
    def on_descendant_focus(self, event: DescendantFocus) -> None:

        # DISPATCH SELECTED LANE WHEN A CHILD WIDGET RECEIVES FOCUS
        self.post_lane_selected()

    # LISTENER: ON LIST VIEW SELECTED
    def on_list_view_selected(self, event: ListView.Selected) -> None:

        # GET SELECTED ITEM
        selected_item = event.item

        # GET TASK
        task_widget = selected_item.query_one(TaskWidget)
        task = task_widget.task

        # DISPATCH SELECTED TASK
        self.post_message(self.TaskSelected(task))

    # LISTENER: ON LIST VIEW HIGHLIGHTED
    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:

        # CHECK FOR EVENTS
        if event.item is None:
            return

        # GET SELECTED ITEM
        selected_item = event.item

        # GET TASK
        task_widget = selected_item.query_one(TaskWidget)
        task = task_widget.task

        # DISPATCH SELECTED TASK
        self.post_message(self.TaskSelected(task))
