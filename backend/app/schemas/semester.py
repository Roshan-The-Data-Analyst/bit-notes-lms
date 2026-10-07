from pydantic import BaseModel


class SemesterBase(BaseModel):
    name: str
    description: str | None = None


class SemesterCreate(SemesterBase):
    level_id: int


class SemesterResponse(SemesterBase):
    id: int
    level_id: int

    class Config:
        from_attributes = True
