import os
import sqlite3
from dotenv import load_dotenv

from vanna import Agent
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.integrations.openai import OpenAILlmService

load_dotenv()


class DefaultUserResolver(UserResolver):
    """Resolves all users to a default user."""

    async def resolve_user(self, request_context: RequestContext) -> User:
        # FIX: Must use id, not user_id
        return User(id="default_user")


def create_vanna_agent():
    """Initialize Vanna Agent with Groq + SQLite + Memory"""

    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    # Groq via OpenAI-compatible API
    llm = OpenAILlmService(
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile"
    )

    # SQLite connection
    conn = sqlite3.connect("clinic.db")
    sqlite_runner = SqliteRunner(conn)

    # Memory
    memory = DemoAgentMemory()

    # Tool registry
    tool_registry = ToolRegistry()
    tool_registry.tools = [
        RunSqlTool(sqlite_runner),
        VisualizeDataTool(),
        SaveQuestionToolArgsTool(),
        SearchSavedCorrectToolUsesTool(),
    ]

    # User resolver
    user_resolver = DefaultUserResolver()

    # Create agent
    agent = Agent(
        llm,
        tool_registry,
        user_resolver,
        memory
    )

    return agent, memory