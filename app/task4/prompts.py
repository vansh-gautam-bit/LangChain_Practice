from langchain_core.prompts import ChatPromptTemplate

summary_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in summarize. write a concise summary of the given topic."
        ),
        (
            "human",
            "{topic}"
        ),
    ]
)

tweet_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a social media expert. Write an engaging tweet about the given topic. Keep it under 280 characters."
        ),
        (
            "human",
            "{topic}"
        ),
    ]
)

linkedin_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional content writer, write a LinkedIn post about the given topic."
        ),
        (
            "human",
            "{topic}"
        )
    ]
)