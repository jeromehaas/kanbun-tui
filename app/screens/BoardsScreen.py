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
from app.services.BoardsService import BoardsService
from app.services.TasksService import TasksService
from app.widgets.BoardsContainerWidget import BoardsContainerWidget
from app.widgets.LanesContainerWidget import LanesContainerWidget


# MAIN SCREEN CLASS FOR DISPLAYING BOARDS AND TASKS
class BoardsScreen (Screen):

    def __init__(self):
        super().__init__()

        # LOAD DOTENV
        load_dotenv()

        # CREATE API CLIENTS
        api_client = ApiClient(base_url=os.getenv("API_BASE_URL"), token=os.getenv("API_TOKEN"))
        tasks_api = TasksApi(api_client)
        boards_api = BoardsApi(api_client)
        self.tasks_service = TasksService(tasks_api)
        self.boards_service = BoardsService(boards_api)



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

            # LOG
            yield Log(id="debug")

