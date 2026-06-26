from app.core.llm import llm
from app.task2.prompts import resume_parser_prompt
from app.task2.schemas import Resume

structured_llm = llm.with_structured_output(Resume)

resume_chain = (
    resume_parser_prompt
    | structured_llm
)