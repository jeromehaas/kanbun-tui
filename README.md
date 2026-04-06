# [TUI] Kanbun

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Textual](https://img.shields.io/badge/Textual-TUI-purple)

Kanbun TUI is the terminal-based interface for the Kanbun project, built with Python and Textual. It provides a focused and keyboard-friendly way to view, manage, and update kanban boards directly from the terminal. The TUI communicates with the Kanbun server to display project data and support day-to-day task management.

## Requirements
- Python
- A reachable and configured kanbun-server

## Installation
Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment variables
Create a `.env` file in the project root:

```env
# API CONNECTION TO SERVER
API_BASE_URL=
API_TOKEN=
```

## Run the application
In the root of the application, run this command:

```bash
python -m app.main
```
