import os
import json

from textual.reactive import reactive
from dotenv import load_dotenv
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Static, ListView, Label, ListItem, Header, Footer, Log
from app.api.ApiClient import ApiClient
from app.api.BoardsApi import BoardsApi
from app.api.TasksApi import TasksApi
from app.api.LanesApi import  LanesApi
from app.models.Board import Board
from app.services.BoardsService import BoardsService
from app.services.TasksService import TasksService
from app.services.LanesService import LanesService
from app.widgets.BoardsContainerWidget import BoardsContainerWidget
from app.widgets.LanesContainerWidget import LanesContainerWidget


# MAIN SCREEN CLASS FOR DISPLAYING BOARDS AND TASKS
class BoardsScreen (Screen):

    selected_board = reactive("None", recompose=True)

    def __init__(self):
        super().__init__()

        # LOAD DOTENV
        load_dotenv()

        # CREATE API CLIENTS
        api_client = ApiClient(base_url=os.getenv("API_BASE_URL"), token=os.getenv("API_TOKEN"))
        tasks_api = TasksApi(api_client)
        boards_api = BoardsApi(api_client)
        lanes_api = LanesApi(api_client)
        self.tasks_service = TasksService(tasks_api)
        self.boards_service = BoardsService(boards_api)
        self.lanes_service = LanesService(lanes_api)


    # DO AT MOUNT OF SCREEN (EXAMPLE FOR LATER)
    # async def on_mount(self):
    #     tasks =  await self.tasks_service.get_all_tasks()
    #     list_view = self.query_one("#tasks_list", ListView)

    #    for task in tasks:
     #       await list_view.append(ListItem(Label(task.title)))

    async def on_mount(self):
        boards = await self.boards_service.get_all_boards()

        log = self.query_one("#debug", Log)
        log.write_line("Data received")

        widget = self.query_one(BoardsContainerWidget)
        widget.boards = boards

        if boards is not None:
            self.selected_board = boards[0].id
        else:
            self.selected_board = ""

        lanes = await self.lanes_service.get_all_lanes(25)
        lanes_widget = self.query_one(LanesContainerWidget)
        lanes_widget.lanes = lanes

    # COMPOSE ALL CHILD WIDGETS
    def compose(self):

        # MAIN AREA CONTAINER
        with Container(id="main-area"):

            # HEADER
            yield Header()

            # MAIN CONTENT
            yield BoardsContainerWidget()
            yield LanesContainerWidget()


            # FOOTER
            yield Footer()

            yield Label(str(self.selected_board))

            # LOG
            yield Log(id="debug")

    def on_boards_container_widget_board_selected(self, event: BoardsContainerWidget.BoardSelected) -> None:
        board = event.board

        log = self.query_one("#debug", Log)
        log.write_line(f"Gewähltes Board:{board.name}")

        self.selected_board = board.id

        # lanes = await self.lanes_service.get_all_lanes(self.selected_board)
        # lanes_widget = self.query_one(LanesContainerWidget)
        # lanes_widget.lanes = lanes
