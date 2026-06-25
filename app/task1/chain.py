from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser

from app.core.llm import llm

from app.task1.prompts import(
    summarize_prompt,
    translate_prompt,
    tone_shift_prompt,
)

summarize_chain = (
    summarize_prompt
    | llm 
    | StrOutputParser()
)

translate_chain = (
    translate_prompt
    | llm
    | StrOutputParser()
)

tone_shift_chain =(
    tone_shift_prompt
    | llm
    | StrOutputParser()
)

transform_chain = RunnableBranch(
    (
        lambda x: x["action"] == "summarize",
        summarize_chain,
    ),
    (
        lambda x: x["action"] == "translate",
        translate_chain,
    ),
    tone_shift_chain
)