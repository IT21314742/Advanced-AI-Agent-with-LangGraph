from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph import StateGraph, START, END
load_dotenv()
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field


load_dotenv()

llm = init_chat_model("gpt-4o")

class state(TypedDict):
    messages: Annotated[list, add_messages]
    user_question: str | None
    google_results: str | None
    bing_results: str | None
    reddit_results: str | None
    selected_reddit_urls: list[str] 