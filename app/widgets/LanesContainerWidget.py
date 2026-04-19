from textual.app import ComposeResult
from textual.widgets import Label, ListView, ListItem
from textual.containers import HorizontalScroll
from textual.reactive import reactive
from app.widgets.LaneWidget import LaneWidget

# CLASS: LANES CONTAINER WIDGET
class LanesContainerWidget(HorizontalScroll):

    # DEFINE LANES
    lanes = reactive([], recompose=True)

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # PRINT LABEL
        yield Label("Lanes")

        # PRINT MESSAGE IF NO LANES ARE AVAILABLE
        if not self.lanes:
            yield Label("No Lanes")
            return

        # LOOP OVER LANES
        for lane in self.lanes:

            # GET LANE WIDGET AND ASSIGN LANE TO IT
            lane_widget = LaneWidget()
            lane_widget.lane = lane

            # PRINT LANE WIDGET
            yield lane_widget