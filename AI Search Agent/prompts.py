from typing import Dict, Any


class PromptsTemplates:
    """Container for all prompt templates used in the research assistant."""
    
    @staticmethod
    def reddit_url_analysis_system() -> str:
        """System prompt for analyzing Reddit URLs."""
        return """You are an expert at analyzing social media content. Your task is to examine Reddit search results and identify the most relevent posts that would provide valuable additional information for answering the user's question
        
        
Analyze the provided Reddit results and identify URLs of the posts that contain valueble information worth investigating further. Focus on posts that:
- Directly address to the user's question
- Official websites, documentation, and reliable sources
- Key statistics, dates, and verified information
- Any conflicting information from Different sources 



Provide a concise analysis highlighting the most relevent findings."""


    @staticmethod
    def google_analysis_user(user_question: str, google_results: str) -> str:
        """User prompt for analyzing Google search results."""
        return f"""Question: {user_question}

Google Search Results: {google_results}

Please analyze these Google results and extract the key insights that help answer the question."""
    
    @staticmethod
    def bing_analysis_system() -> str:
        """System prompt for"""


