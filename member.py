from pydantic import BaseModel, ConfigDict


class MemberBase(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    id: int

    model_config = ConfigDict(from_attributes=True)