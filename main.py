from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_core.core_schema import model_field
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI

# load api keys
load_dotenv()
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# model of llm
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
                             google_api_key=gemini_api_key,
                             temperature=0.3
                             )

todoist = TodoistAPI(todoist_api_key)
# tool decorator, so llm can access
@tool
def add_task(task, desc=None):
    """Add a new task to the user's task list.
        Use this when the user wants to create or add a task to the list"""
    todoist.add_task(content=task, description=desc)

@tool
def remove_task(task_id):
    """Remove a task from the user's task list."""
    todoist.delete_task(task_id)

@tool
def get_tasks():
    """Gets all the tasks from users list, which also shows the ids of the tasks, which
        is utilized for the remove task tool"""
    return todoist.get_tasks()

@tool
def show_tasks():
    """Get all tasks from the user's task list, and immediately show them"""
    results = todoist.get_tasks()
    tasks = []
    for task in results:
        for task_content in task:
            tasks.append(task_content.content)
    return tasks

@tool
def exit_program():
    """ if user explicitly wants to to exit the program, use this tool to exit"""
    exit()

tools = [add_task, remove_task, get_tasks, show_tasks, exit_program]

system_prompt = "You are a helpful assistant, that will assist the user with adding tasks"

prompt = ChatPromptTemplate.from_messages([("system", system_prompt),
                                           ("user", "{input}"),
                                           MessagesPlaceholder("agent_scratchpad"),
                                           MessagesPlaceholder("history")])

# initialize the agent
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# history of current interaction
history = []

# main loop
while True:
    user_prompt = input("Enter instruction: ")
    try:
        response = agent_executor.invoke({"input": user_prompt, "history": history})
        print(response['output'])
        history.append(HumanMessage(content=user_prompt))
        history.append(AIMessage(content=response['output']))
    except Exception as e:
        print(e)