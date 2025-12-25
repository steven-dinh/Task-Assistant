# Task Manager Agent

A simple, AI-powered task management assistant built with Python, LangChain, and Google's Gemini. This agent allows you to manage your Todoist tasks using natural language.

## Features

- **Natural Language Interaction**: Add, remove, and view tasks by chatting with the agent.
- **Todoist Integration**: Syncs directly with your Todoist account.
- **Powered by Gemini**: Uses Google's Gemini 2.5 Flash model for intelligent task parsing and execution.

## Prerequisites

- Python 3.12+
- A [Todoist](https://todoist.com/) account and an [API Key](https://todoist.com/app/settings/integrations/developer).
- A [Google Gemini API Key](https://aistudio.google.com/app/apikey).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd "Task Manager Agent"
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory of the project and add your API keys:

```env
TODOIST_API_KEY=your_todoist_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the main script to start the interactive agent:

```bash
python main.py
```

Once started, you can enter instructions like:
- "Add a task to buy milk today"
- "Show me all my tasks"
- "Remove the task with ID 123456789"
- "Exit"

## Available Tools

The agent is equipped with the following tools:
- `add_task`: Add a new task to your Todoist list.
- `remove_task`: Delete a task using its ID.
- `get_tasks`: Retrieve all tasks (includes IDs for removal).
- `show_tasks`: List all task contents.
- `exit_program`: Close the application.
