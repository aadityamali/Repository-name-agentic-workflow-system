from typing import TypedDict


class AgentState(TypedDict):
    query: str
    plan: str
    context: str
    answer: str
    evaluation: str