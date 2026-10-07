from pydantic import BaseModel


class QuestionCreate(BaseModel):
    quiz_id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: str | None = None
    order: int = 0


class QuestionResponse(QuestionCreate):
    id: int

    class Config:
        from_attributes = True
