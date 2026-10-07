from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str | None = None
    image_url: str | None = None
    pdf_url: str | None = None
    video_url: str | None = None
    order: int = 0


class NoteCreate(NoteBase):
    topic_id: int


class NoteResponse(NoteBase):
    id: int
    topic_id: int

    class Config:
        from_attributes = True
