from pydantic import BaseModel, ConfigDict
from datetime import date


class BorrowRecordBase(BaseModel):
    book_id: int
    member_id: int
    borrow_date: date


class BorrowRecordCreate(BorrowRecordBase):
    pass


class BorrowRecordResponse(BorrowRecordBase):
    id: int
    return_date: date | None = None

    model_config = ConfigDict(from_attributes=True)