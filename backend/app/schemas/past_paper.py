from pydantic import BaseModel


class PastPaperCreate(BaseModel):
    module_id: int
    title: str
    year: int | None = None
    semester: str | None = None
    description: str | None = None
    pdf_url: str


class PastPaperResponse(PastPaperCreate):
    id: int

    class Config:
        from_attributes = True
