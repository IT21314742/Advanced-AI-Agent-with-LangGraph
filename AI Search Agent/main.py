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
    selected_reddit_urls: list[str] | None
    reddit_post_data: list | None
    google_analysis: str | None
    bing_analysis: str | None
    reddit_analysis: str | None
    final_answer: str | None

def google_search(state: State):
    return

def bing_search(state: State):
    return

def reddit_search(state: State):
    return

def analyze_reddit_posts(state: State):
    return

def analyze_google_results(state: State):
    return

def analyze_bing_results(state: State):
    return

def synthesize_analysis(state: State):
    return

graph_builder = StateGraph(State)

graph_builder.add_node("google_search", google_search)
graph_builder.add_node("bing_search",)