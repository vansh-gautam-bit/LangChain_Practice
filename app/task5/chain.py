from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda

from app.core.llm import llm

from app.task5.prompts import (
    extract_prompt,
    repair_prompt
)

from app.task5.schemas import UserInfo

parser = JsonOutputParser(pydantic_object=UserInfo)

extract_chain = (
    extract_prompt
    | llm
)

def safe_parse(x):

    try:

        return parser.invoke(x)
    except Exception as e:
        repaired =(
            repair_prompt
            | llm
        ).invoke(
            {
                "output": x.content,
                "error": str(e),
            }
        )

        return parser.invoke(repaired)
    
safe_json_chain = (
    extract_chain
    | RunnableLambda(safe_parse)
)    