from pydantic import BaseModel, Field, field_validator
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

class ReferencedResponse(BaseModel):
    answer: str = Field(
        description="The conversational answer. Must include inline citations [1] and a '# References' section at the end."
    )
    used_ids: List[int] = Field(description="The list of IDs used in the citations.")

    @field_validator('answer')
    @classmethod
    def check_references_section(cls, v: str) -> str:
        if "# References" not in v:
            raise ValueError("The response must include a '# References' section.")
        return v


llm: ChatOpenAI = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm = llm.with_structured_output(ReferencedResponse) # type: ignore

system_prompt = """You are a focused RAG Assistant. 
You will be provided with:
1. SEARCH_RESULTS: Chunks from our knowledge base.
2. CONVERSATION_HISTORY: Previous messages.

Your goal is to answer the USER_QUERY using ONLY the provided search results. 
If the history provides context (like what 'it' refers to), use it.
Always cite your sources by ID."""

prompt = ChatPromptTemplate.from_messages([ # type: ignore
    ("system", system_prompt),
    ("human", "CONVERSATION_HISTORY: {history}\n\nSEARCH_RESULTS: {context}\n\nUSER_QUERY: {query}")
])

rag_chain = prompt | structured_llm # type: ignore

history_data = "User: Who is the CEO of Apple? AI: Tim Cook. User: How long has he been there?"
context_data = "[ID: 101] Tim Cook became CEO in 2011. [ID: 102] He joined Apple in 1998."

result = rag_chain.invoke({ # type: ignore
    "history": history_data,
    "context": context_data,
    "query": "Since when?"
})

# 5. Inspect the "Structured" Result
print(result) # type: ignore