from typing import Dict, Any


class PromptsTemplates:
    """Container for all prompt templates used in the research assistant."""
    
    @staticmethod
    def reddit_url_analysis_system() -> str:
        """System prompt for analyzing Reddit URLs."""
        return """You are an expert at analyzing social media content. Your task is to examine Reddit search results and identify the most relevent posts that would provide valuable additional information for answering the user's question

        
        
        
Analyze the provided Reddit results and identify URLs of the posts that contain valueble information worth investigating further. Focus on posts that:
- Directly address to the user's question
- Contain detailed discussions or expert opinions
- Have high engagement (upvotes, comments)
- Provide unique perspectives or insights 

Return a structured response with the selected URLs."""

    @staticmethod
    def reddit_url_analysis_user(user_question: str, reddit_results: str) -> str:
        """User prompt for analyzing Reddit URLs."""
        return f"""User Question: {user_question}

reddit Results: {reddit_results}

Please analyze these reddit results and identify the most valuable posts for answering the user's question."""
    
    @staticmethod
    def google_analysis_system() -> str:
        """System prompt for analyzing google search results."""
        return """You are an expert research analyst. Analyze the provided Google search results to extract key insights that answer the user's question.

Focus on:
- Main factual information and athoritative sources
- Official websites, documentation, and reliable publications
- key statistics, dates, and verified information
- Any conflicting information from different sources


Provide a concise analysis highlighting the most relevant findings."""

    @staticmethod
    def 