from langchain_core.prompts import ChatPromptTemplate

classifier_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a query classifier.
            
            Classify the users question into exactly one category:
            
            - coding
            - math
            - general
            """
        ),
        (
            "human",
            "{question}"
        ),
    ]
)

coding_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert software engineer. Give clear, correct coding answers."
        ),
        (
            "human",
            "{question}"
        ),
    ]
)
math_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert mathematician. Solve the problem step by step."
        ),
        (
            "human",
            "{question}"
        ),
    ]
)

general_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Tou are knowledg AI assisstant."
        ),
        (
            "human",
            "{question}"
        ),
    ]
)