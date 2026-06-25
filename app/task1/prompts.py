from langchain_core.prompts import ChatPromptTemplate

summarize_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert at summarizing text. Produce a cincise and accurate summary."
        ),
        (
            "human",
            "{text}"
        )
    ]
)

translate_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional translator. translate the given text into {language}."
        ),
        (
            "human",
            "{text}"
        )
    ]
)

tone_shift_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Rewrite the text in a professional and polite tone without changing its meaning. "
        ),
        (
            "human",
            "{text}"
        )
    ]
)