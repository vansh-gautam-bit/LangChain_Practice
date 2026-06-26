from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda

from app.core.llm import llm

from app.task5.prompts import (
    extract_prompt,
    repair_prompt
)

from app.task5.schemas import UserInfo

parser = PydanticOutputParser(pydantic_object=UserInfo)

extract_chain = (
    extract_prompt
    | llm
)

def safe_parse(ai_message):
    raw_output = ai_message.content

    try:

        return parser.parse(raw_output)
    
    except Exception as e:

        repair_chain =(
            repair_prompt
            | llm
        )

        fixed_output = repair_chain.invoke(
            {
                "output": raw_output,
                "error": str(e),
            }
        )

        try:
            return parser.parse(fixed_output.content)
        
        except Exception:
            raise ValueError(
                "Unable to generate valid JSON after retry."
            )
    
safe_json_chain = (
    extract_chain
    | RunnableLambda(safe_parse)
)    