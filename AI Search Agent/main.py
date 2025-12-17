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
    print(f"Searching Reddit for: {user_question}")


    reddit_results = reddit_search_api(keyword=user_question)
    print(reddit_results)


    return {"reddit_results": reddit_results}


def analyze_reddit_posts(state: State):
    user_question = state.get("user_question","")
    reddit_results = state.get("reddit_results", "")

    if not reddit_results:
        return {"selected_reddit_urls": []}
    
    structured_llm = llm.with_structutred_output(RedditURLAnalysis)
    messages = get_reddit_url_analysis_messages(user_question, reddit_results)


    try:
        analysis = structured_llm.invoke(messages)
        selected_urls = analysis.selected_urls
        

        print("Selected URLs:")
        for i, url in enumerate(selected_urls, 1):
            print(f"    {i}. {url}")


    except Exception as e:
        print(e)
        selected_urls = []

    return {"selected_reddit_urls": selected_urls}



def retrieve_reddit_posts(state: State):
    print("Getting reddit post comments")


    selected_urls = state.get("selected_reddit_urls", [])


    if not selected_urls:
        return {"reddit_post_data": []}
    
    print(f"Processing {len(selected_urls)} Reddit URLs")

    reddit_post_data = reddit_post_retrieval(selected_urls)

    if reddit_post_data:
        print(f"Successfully got {len(reddit_post_data)} posts")
    else:
        print("Failed to get post data")
        reddit_post_data = []

    
    print(reddit_post_data)
    return {"reddit_post_data": reddit_post_data}


def analyze_google_results(state: State):
    print("Analyzing google search results")


    user_question = state.get("user_question","")
    google_results = state.get("google_results", "")

    messages = get_google_analysis_messages(user_question, google_results)
    reply = llm.invoke(messages)


    return {"google_analysis": reply.content}


def analyze_bing_results(state: State):
    print("Analyzing Bing search results")

    user_question = state.get("user_question", "")
    bing_results = state.get("bing_results", "")

    messages = get_bing_analysis_messages(user_question, bing_results)
    reply = llm.invoke(messages)

    return {"bing_analysis": reply.content}


def analyze_reddit_results(state: State):
    print("Analyzing reddit search results")


    user_question = state.get("user_question", "")
    reddit_results = state.get("reddit_results",  "")
    reddit_post_data = state.get("reddit_post_data", "")

    messages = get_reddit_analysis_messages(user_question, reddit_results, reddit_post_data)
    reply = llm.invoke(messages)

    