from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str

class BookRead(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
