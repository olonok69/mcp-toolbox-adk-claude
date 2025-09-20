from google.adk.agents.llm_agent import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load all the tools
tools = toolbox.load_toolset('my-toolset')


root_agent = Agent(
    name="gcp_hotel_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about hotels in BigQuery."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about hotels in BigQuery. Use the tools to answer the question"
    ),
    tools=tools,
)