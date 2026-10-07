from pydantic import BaseModel, Field


class ProgressCreate(BaseModel):
    user_id: int
    note_id: int
    completion_percentage: float = Field(default=0, ge=0, le=100)


class ProgressResponse(ProgressCreate):
    id: int

    class Config:
        from_attributes = True
