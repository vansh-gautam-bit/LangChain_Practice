from langchain_core.prompts import ChatPromptTemplate
resume_parser_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are expert resume parser. Extract the candidate name, skills, years of professional experience and most recent job role. If a field is missing, make your best reasonable inference or leave it empty."
        ),
        (
            "human",
            "{resume_text}"
        ),
    ]
)