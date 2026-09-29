from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    category: str
    price: float
    available_copies: int
    isbn: str | None = None


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    is_available: bool

    model_config = ConfigDict(from_attributes=True)