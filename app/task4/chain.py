from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from app.core.llm import llm2

from app.task4.prompts import (
    summary_prompt,
    tweet_prompt,
    linkedin_prompt,
)

from langchain_core.runnables import(
    RunnableParallel,
    RunnablePassthrough,
)

summary_chain = (
    summary_prompt
    | llm2
    | StrOutputParser() 
)

tweet_chain = (
    tweet_prompt
    |llm2
    | StrOutputParser()
)

linked_chain = (
    linkedin_prompt
    | llm2
    | StrOutputParser()
)

content_chain = (
    RunnablePassthrough()
    | RunnableParallel(
    summary=summary_chain,
    tweet=tweet_chain,
    linkedin_post=linked_chain,
    )
)