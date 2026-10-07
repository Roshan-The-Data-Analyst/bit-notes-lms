from pydantic import BaseModel


class ModuleBase(BaseModel):
    code: str
    name: str
    description: str | None = None
    credits: int | None = None
    image_url: str | None = None


class ModuleCreate(ModuleBase):
    semester_id: int


class ModuleResponse(ModuleBase):
    id: int
    semester_id: int

    class Config:
        from_attributes = True
