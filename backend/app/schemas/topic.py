from pydantic import BaseModel


class TopicBase(BaseModel):
    title: str
    description: str | None = None
    order: int = 0


class TopicCreate(TopicBase):
    module_id: int


class TopicResponse(TopicBase):
    id: int
    module_id: int

    class Config:
        from_attributes = True
