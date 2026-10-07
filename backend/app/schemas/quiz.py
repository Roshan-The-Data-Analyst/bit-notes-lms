from pydantic import BaseModel


class QuizBase(BaseModel):
    title: str
    description: str | None = None


class QuizCreate(QuizBase):
    note_id: int | None = None


class QuizResponse(QuizBase):
    id: int
    note_id: int | None = None

    class Config:
        from_attributes = True
