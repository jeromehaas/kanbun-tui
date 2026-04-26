# [TUI] Kanbun

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Textual](https://img.shields.io/badge/Textual-TUI-purple)

Kanbun TUI is the terminal-based interface for the Kanbun project, built with Python and Textual. It provides a focused
and keyboard-friendly way to view, manage, and update kanban boards directly from the terminal. The TUI communicates
with the Kanbun server to display project data and support day-to-day task management.

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
```

## Run the application
In the root of the application, run this command:

```bash
textual run app.main:Kanbun
```

## Run the application in developer move
If you want to run the application while development, run this command:

```bash
textual run app.main:Kanbun --dev
```

Next, open a new terminal session and run the logs:

```bash
textual console
```

## Create a global command
If you want to make the application globally available on your client, follow the steps below.

Create a new file in `~/.local/bin`:

```bash
mkdir -p ~/.local/bin
vim ~/.local/bin/kanbun
```

Then add this inside:

```
#!/usr/bin/env bash                                                                                                 

# LET PROGRAMM FAIL
set -euo pipefail                                                                                                   

# SETUP PROJECT DIRECTORY
KANBUN_DIR="$HOME/${PATH_TO_APP}/kanbun-tui"

# CD INTO PROJECT DIRECTORY
cd "$KANBUN_DIR"
                                                                                                                    
# CREATE AND ACTIVATE ENVIRONMENT
python3 -m venv .venv                                                                                               
source ".venv/bin/activate"

# RUN APP
exec textual run  app.main:Kanbun  
```

Make sure the command is executable:
```bash
chmod +x ~/.local/bin/kanbun
```

Make sure the path is available:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc # IF YOU USE BASH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc # IF YOU USE ZSH
```

Also, reload your config:
```
source ~/.bashrc # IF YOU USE BASH
source ~/.zshrc # IF YOU USE ZSH
```

Then run the app from anywhere by entering the command:
```bash
kanbun
```
