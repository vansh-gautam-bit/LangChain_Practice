from langchain_core.prompts import ChatPromptTemplate

extract_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Extract the requested information from the user text and return it in JSON format."
        ),
        (
            "human",
            "{text}"
        ),
    ]
)

repair_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            The previous JSON could not be parsed
            Fix the JSON using the parser error.
            Return ONLY valid JSON.
            """
        ),
        (
            "human"
            """
            Original Output:
            {output}

            ParserError:
            {error}
            """
        ),
    ]
)