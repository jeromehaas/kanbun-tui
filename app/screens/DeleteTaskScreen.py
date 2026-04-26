import os
from textual.app import App
from textual.screen import Screen
from textual.widgets import Label, Button, Input, TextArea
from textual.containers import Grid
from app.api.ApiClient import ApiClient
from app.api.TasksApi import TasksApi
from app.models.Task import Task
from app.services import TasksService

# CLASS: DELETE TASK SCREEN
class DeleteTaskScreen (Screen):
    def __init__(self, selected_board, selected_lane, selected_task):
        super().__init__()
        self.board = selected_board
        self.lane = selected_lane
        self.edit_task = selected_task

        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # CREATE SERVICES
        self.tasks_api = TasksApi(api_client)
        self.tasks_service = TasksService(self.tasks_api)

    # COMPOSE ALL ELEMENTS
    def compose(self):
        yield Grid(
            Label("Delete Task", id="title"),
            Label(f"Do you want to delete the task <{self.edit_task.title}>?", id="question"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK", variant="primary", id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":
            # DELETE DATA
            await self.tasks_service.delete_task(self.board, self.lane, self.edit_task)

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":
            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()