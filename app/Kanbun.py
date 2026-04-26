from textual.app import App
from app.screens.BoardsScreen import BoardsScreen
from app.screens.CreateBoardScreen import CreateBoardScreen
from app.screens.DeleteBoardScreen import DeleteBoardScreen
from app.screens.EditBoardScreen import EditBoardScreen


# CLASS: MAIN CLASS FOR KANBUN APPLICATION
class Kanbun(App):
    # PATHS TO CSS FILES
    CSS_PATH = ["./styles/global.tcss",
                "./styles/screens/boards-screen.tcss",
                "./styles/widgets/boards-container-widget.tcss",
                "./styles/widgets/lanes-container-widget.tcss",
                "./styles/widgets/board-tile-widget.tcss",
                "./styles/widgets/task-widget.tcss",
                "./styles/widgets/lane-widget.tcss",
                "./styles/screens/delete-board-screen.tcss",
                "./styles/screens/delete-lane-screen.tcss",
                "./styles/screens/create-lane-screen.tcss",
                "./styles/screens/create-board-screen.tcss",
                "./styles/screens/edit-board-screen.tcss",
                "./styles/screens/edit-lane-screen.tcss",
                "./styles/screens/create-task-screen.tcss",
                "./styles/screens/edit-task-screen.tcss",
                "./styles/screens/delete-task-screen.tcss",
                ]

    # HOOK: ON MOUNT
    def on_mount(self) -> None:
        self.install_screen(BoardsScreen(), name='BoardsScreen')
        self.install_screen(DeleteBoardScreen(), name="DeleteBoardScreen")
        self.install_screen(CreateBoardScreen(), name="CreateBoardScreen")
        self.install_screen(EditBoardScreen(), name="EditBoardScreen")
        self.push_screen("BoardsScreen")
