from textual.screen import Screen
from textual.widget import Text
from textual.widgets import Static

# MAIN SCREEN CLASS FOR DISPLAYING BOARDS AND TASKS
class BoardsScreen (Screen):
    CSS_PATH = "../styles/boards-screen.tcss"

    # COMPOSE ALL CHILD WIDGETS
    def compose(self):
        yield Static("Hello World")