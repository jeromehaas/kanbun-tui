from textual.app import App
from app.screens.BoardsScreen import BoardsScreen

# MAIN CLASS FOR KANBUN APPLICATION
class Kanbun(App):
    CSS_PATH = ["./styles/screens/boards-screen.tcss","./styles/widgets/boards-container.tcss","./styles/widgets/lanes-container.tcss","./styles/widgets/board-tile.tcss","./styles/widgets/task-widget.tcss","./styles/widgets/lane-widget.tcss"]

    # BUILD ON MOUNT OF APPLICATION
    def on_mount(self) -> None:
        self.install_screen(BoardsScreen(), name='BoardsScreen')
        self.push_screen("BoardsScreen")