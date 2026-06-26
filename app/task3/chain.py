from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

from app.core.llm import llm

from app.task3.prompts import(
    classifier_prompt,
    coding_prompt,
    math_prompt,
    general_prompt
)

from app.task3.schemas import Classification

classifier_llm = llm.with_structured_output(Classification)

classifier_chain = (
    classifier_prompt
    | classifier_llm
)
router_chain = RunnableBranch(
    (
        lambda x: x["category"] == "coding",
        coding_prompt | llm | StrOutputParser(),
    ),
    (
        lambda x: x["category"] == "math",
        math_prompt | llm | StrOutputParser(),
    ),
    general_prompt | llm | StrOutputParser(),
)

ask_chain = (
    RunnableLambda(
        lambda x: {
            "category": classifier_chain.invoke(x).category,
            "question": x["question"],
        }
    )
    | router_chain
)