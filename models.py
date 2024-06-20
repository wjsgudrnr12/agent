from pydantic import BaseModel

class AIAgentQuery(BaseModel):
    query: str


class File(BaseModel):
    path: str
