from pydantic import BaseModel


class BookmarkCreate(BaseModel):
    user_id: int
    note_id: int


class BookmarkResponse(BookmarkCreate):
    id: int

    class Config:
        from_attributes = True
