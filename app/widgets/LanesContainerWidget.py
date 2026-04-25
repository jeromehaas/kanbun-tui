from types import SimpleNamespace

from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import HorizontalScroll
from textual.reactive import reactive
from app.widgets.LaneWidget import LaneWidget


# CLASS: LANES CONTAINER WIDGET
class LanesContainerWidget(HorizontalScroll):

    # DEFINE LANES
    lanes = reactive([], recompose=True)
    selected_lane_id = reactive(None, recompose=True)
    selected_task_id = reactive(None, recompose=True)

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # PRINT LABEL
        yield Label("Lanes")

        # IF NO LANES ARE AVAILABLE, PRINT 5 PLACEHOLDER LANES
        if not self.lanes:
            for i in range(1):
                lane_widget = LaneWidget()
                lane_widget.lane = SimpleNamespace(
                    name=f" ",
                    tasks=[],
                )
                yield lane_widget
            return

        # LOOP OVER LANES
        for lane in self.lanes:
            lane_widget = LaneWidget()
            lane_widget.lane = lane
            if lane.id == self.selected_lane_id:
                lane_widget.selected_task_id = self.selected_task_id
            yield lane_widget
