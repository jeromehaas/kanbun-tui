import os
from dotenv import load_dotenv
from textual.screen import Screen
from textual.widgets import Static, ListView, Label, ListItem
from app.api.ApiClient import ApiClient
from app.api.TasksApi import TasksApi
from app.services.TasksService import TasksService

# MAIN SCREEN CLASS FOR DISPLAYING BOARDS AND TASKS
class BoardsScreen (Screen):
    CSS_PATH = "../styles/screens/boards-screen.tcss"

    def __init__(self):
        super().__init__()

        # LOAD DOTENV
        load_dotenv()

        # CREATE API CLIENTS
        api_client = ApiClient(base_url=os.getenv("API_BASE_URL"), token=os.getenv("API_TOKEN"))
        tasks_api = TasksApi(api_client)
        self.tasks_service = TasksService(tasks_api)

    # DO AT MOUNT OF SCREEN
    async def on_mount(self):
        tasks =  await self.tasks_service.get_all_tasks()
        list_view = self.query_one("#tasks_list", ListView)

        for task in tasks:
            await list_view.append(ListItem(Label(task.title)))

    # COMPOSE ALL CHILD WIDGETS
    def compose(self):
        yield Static("Hello World")
        yield ListView(id="tasks_list")