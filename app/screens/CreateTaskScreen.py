import os
from textual.screen import Screen
from textual.widgets import Label, Button, Input, TextArea
from textual.containers import Grid
from app.api.ApiClient import ApiClient
from app.api.TasksApi import TasksApi
from app.models.Task import Task


# SCREEN CLASS FOR CREATE A TASK
class CreateTaskScreen(Screen):

    def __init__(self, selected_board, selected_lane):
        super().__init__()


        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # CREATE SERVICES
        self.tasks_api = TasksApi(api_client)

    # COMPOSE ALL ELEMENTS
    def compose(self):
        yield Grid(
    Label("Create New Task", id="title"),
            Input(placeholder="Task Title", type="text", id="input_task_title"),
            TextArea(placeholder="Task Description", id="input_task_description"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK",variant="primary" ,id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":

            # GET VALUE FROM INPUTS
            task_title = self.query_one("#input_task_title", Input).value
            task_description = self.query_one("#input_task_description", Input).value

            # WRITE DATA
            data = Task(
                title=task_title,
                description=task_description,
            )

            # POST DATA
            await self.tasks_api.create_task(data)

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()