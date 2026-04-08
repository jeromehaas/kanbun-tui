from textual.app import App
from app.screens.BoardsScreen import BoardsScreen

# MAIN CLASS FOR KANBUN APPLICATION
class Kanbun(App):

    # BUILD ON MOUNT OF APPLICATION
    def on_mount(self) -> None:
        self.install_screen(BoardsScreen(), name='BoardsScreen')
        self.push_screen("BoardsScreen")