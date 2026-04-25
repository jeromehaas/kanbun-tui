import os
from textual.app import App
from textual.screen import Screen
from textual.widgets import Label, Button, Input, TextArea
from textual.containers import Grid
from app.api.ApiClient import ApiClient
from app.api.TasksApi import TasksApi
from app.models.Task import Task
from app.services import TasksService

# CLASS: EDIT TASK SCREEN
class EditTaskScreen (Screen):
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
            Label("Edit Task", id="title"),
            Input(placeholder="Task Title", type="text", id="input_task_title", value=self.edit_task.title),
            TextArea(placeholder="Task Description", id="input_task_description", text=self.edit_task.description),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK", variant="primary", id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":
            # GET VALUE FROM INPUTS
            task_title = self.query_one("#input_task_title", Input).value
            task_description = self.query_one("#input_task_description", TextArea).text

            # WRITE DATA
            data = Task(
                id=self.edit_task.id,
                title=task_title,
                description=task_description,
            )

            # PATCH DATA
            await self.tasks_service.edit_task(self.board, self.lane, data)

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":
            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()