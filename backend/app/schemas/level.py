from pydantic import BaseModel


class LevelBase(BaseModel):
    name: str
    description: str | None = None


class LevelCreate(LevelBase):
    pass


class LevelUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class LevelResponse(LevelBase):
    id: int

    class Config:
        from_attributes = True
