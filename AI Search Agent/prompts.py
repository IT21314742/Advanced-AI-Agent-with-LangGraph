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
    def google_analysis_user(user_question: str, google_results: str) -> str:
        """User prompt for analyzing google search results."""
        return f"""Question: {user_question}

Google Search Results: {google_results}

Please analyze these Google results and extract the key insights that help answer the question."""

    @staticmethod
    def bing_analysis_system() -> str:
        """System prompt for analyzing bing search results."""
        return """You are an expert research analyst. analyze the provided Bing search results to extract complementary insights that answer the user's question
    
Focus on:
- Additional perspective not covered in other resources
- Technical details and documentation
- News articles and recent developments
- Microsoft ecosystem and enterprise perspectives

Provide a concise analysis highlighting unique findings and perspectives"""

    @staticmethod
    def bing_analysis_user(user_question: str, bing_results: str) -> str:
        """User prompt for analyzing Bing search results."""
        return f"""Question: {user_question}


Bing Search Results: {bing_results}

Please analyze these results and extract insights that complement other search sources."""

    @staticmethod
    def reddit_analysis_system() -> str:
        """System prompt for analyzing reddit discussions."""
        return """You are an expert at analyzing spcial media discussions. Analyze the provided Reddit content to extract community insights and user experiences.
        
        
Focus on:
- Real user experiences and testimonials
- Community consensus and popular opinions
- Practical tips and advice from users
- Different perspectives and debates
- Specific quotes from posts and comments
    

IMPORTTANT: When referencing specific content, directly quote it and mention the subreddit or context.
Highlight both positive and negative experiences, controversies, and verying opinions."""

    @staticmethod
    def reddit_analysis_user(
        user_question: str, reddit_results: str, reddit_post_data: list
    ) -> str:
        """User prompt for analyzing Reddit discussions"""
        return f"""Question: {user_question}
    
    Reddit Search Results: {reddit_results}
    
    Detailed Reddit Post Data: {reddit_post_data}
    
    Please analyze this reddit content and extract community insights, user experience, and relevant discussions."""

    @staticmethod
    def synthesis_system() -> str:
        """System prompt for synthesizing all analyses"""
        return """You are an expert research research synthesizer. Combine the provided analysis from different sources to create a comprehensive, well-structured answer.
    
Your task:
- Synthesize insights from Google, Bing, and Reddit analyses
- Identify common themes and conflicting information
- Present a balanced view incorporating different perspectives
- Structure the responses logically with clear sections
- Cite the source type (Google, Bing, Reddit) for key claims
- Highlight and contradictions or uncertainties

Create a comprehensive answer that addresses the user's question from multiple angles."""

    @staticmethod
    def synthesis_user(
        user_question: str,
        google_analysis: str,
        bing_analysis: str,
        reddit_analysis: str,
    ) -> str:
        """User prompt for synthesizing all analysis"""
        return f"""Question: {user_question}
    
    Google Analysis: {google_analysis}
    
    Bing Analysis: {bing_analysis}
    
    Reddit Community Analysis: {reddit_analysis}

    Please synthesize these analysis into a comprehensive answer that addresses the question from multiple perspectives."""


    def create_message_pair(system_prompts: str, user_prompts: str) -> list[Dict[str, Any]]:
        """
        Create a standerdized message pair for LLM interactions.

        args:
            system_prompt: The system message content.
            user_prompt: The user message content.
        
         Returns:   
            List containing system and user message dictionaries
        """
        return [
            {"role": "system": system_prompt},
            {"role": "user", "content": user_prompt},
        ]



# Convenience functions for creating complete message arrays
def get_reddit_url_analysis_message(
        user_question: str, reddit_results: str
) -> list[Dict[str, Any]]:
    """Get message for Reddit URL Analysis"""
    return create_message_pair(
        PromptsTemplates.reddit_url_analysis_system(),
        PromptsTemplates.reddit_url_analysis_user(user_question, reddit_results),
    )

def get_google_analysis_messages(
        user_question: str, google_results: str
) -> list[Dict[str, Any]]:
    """Get messages for Google results analysis"""
    return create_message_pair(
        PromptsTemplates.google_analysis_system(),
        PromptsTemplates.google_analysis_user(user_question, bing_results),
    )


def get_bing_analysis_messages(
        user_question: str, bing_results: str
) -> list[Dict[str, Any]]:
    """Get messages for Bing discussions analysis."""
    return create_message_pair(
        PromptsTemplates.bing_analysis_system(),
        PromptsTemplates.bing_analysis_user(user_question, bing_results),
    )


def get_reddit_analysis_messages(
        user_question: str, reddit_results: str, reddit_post_data: list
) -> list[Dict[str,Any]]:
    """Get messages for Reddit discussions analysis."""
    return create_message_pair(
        PromptsTemplates.reddit_analysis_system(),
        PromptsTemplates.reddit_analysis_user(
            user_question, reddit_results, reddit_post_data
        ),
    )
    
def get_synthesis_messages(
    user_question: str, google_analysis: str, bing_analysis: str, reddit_analysis: str
)                                                        