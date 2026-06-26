from langchain_core.prompts import ChatPromptTemplate

extract_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """"

            Extract the requested information.

            Return ONLY valid JSON

            Fields:

            -name
            -age
            -occuopation
            """
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

            Your previous JSON could not be parsed

            Fix ONLY the JSON.

            Return ONLY valid JSON.

            Do not explain anything.
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