from textual.app import App
from app.screens.BoardsScreen import BoardsScreen

# CLASS: MAIN CLASS FOR KANBUN APPLICATION
class Kanbun(App):

    # PATHS TO CSS FILES
    CSS_PATH = ["./styles/screens/boards-screen.tcss","./styles/widgets/boards-container-widget.tcss","./styles/widgets/lanes-container-widget.tcss","./styles/widgets/board-tile-widget.tcss","./styles/widgets/task-widget.tcss","./styles/widgets/lane-widget.tcss"]

    # HOOK: ON MOUNT
    def on_mount(self) -> None:
        self.install_screen(BoardsScreen(), name='BoardsScreen')
        self.push_screen("BoardsScreen")