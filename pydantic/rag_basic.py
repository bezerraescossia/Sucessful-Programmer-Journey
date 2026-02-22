# Extracting information using LLM
from openai import OpenAI
from typing import Any
from pydantic import (
    BaseModel, Field, field_validator,
    computed_field, ValidationError,
)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import Runnable

load_dotenv()

class ActionItem(BaseModel):
    task: str
    assignee: str

    @field_validator('assignee')
    @classmethod
    def must_be_title_case(cls, v: str) -> str:
        return v.title().strip()


class MeetingSummary(BaseModel):
    topic: str
    actions: list[ActionItem]
    reasoning: str = Field(description="Explain your step-by-step logic for identifying these specific action items.")

    @field_validator('actions')
    @classmethod
    def is_filled(cls, v: list[ActionItem]):
        if len(v) == 0:
            raise ValueError('The AI failed to find any actionable items.')
        else:
            return v
        
    @computed_field
    def action_count(self) -> int:
        return len(self.actions)

# Dummy data for the LLM
data: dict["str", Any] = {
    "topic": "Dummy Meeting",
    "actions": [ActionItem(task="task 1", assignee="bob jones"), ActionItem(task="task 2", assignee="isaac newton")],
    "reasoning": "explanation..."
}

# This is a MeetingSummary object, NOT a string!
llm: ChatOpenAI = ChatOpenAI(model="gpt-4o", temperature=0)
structured_llm: Runnable[Any, MeetingSummary] = llm.with_structured_output(MeetingSummary)
result = structured_llm.invoke("Sarah needs to buy milk and John needs to fix the sink.")


print(f"Action count (computed): {result.action_count}")
for action in result.actions:
    print(f"Assignee (Title-Cased): {action.assignee}")