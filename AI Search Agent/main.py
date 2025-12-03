from dash import State
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

class RedditURLAnalysis(BaseModel):
    selected_urls: list[str] = Field(description= "List of reddit URLs that contain valuable information for answering the user's question")
    
    
def google_search(state: State):
    user_question = state.get("user_question","")
    print(f"Searching Google for: {user_question}")
    
    google_results = serp_search(user_question, engine="google")
    
    
    return {"google_results": google_results}




def bing_search(state: State):
    user_question = state.get("user_question", "")
    print(f"Searching Bing for: {user_question}")
    
    bing_results = serp_search(user_question, engine="bing")
    
    
    return {"bing"}

def reddit_search(state: State):
    user_question = state.get("user_question", "")
    print(f)
    return

