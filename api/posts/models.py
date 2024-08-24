from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from api.core.models import TimestampModel, RecID

prefix = "deploystream"


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: RecID


class UserPostBase(SQLModel):
    body: str = Field(max_length=255, nullable=False)


class UserPosts(
    TimestampModel,
    UserPostBase,
    RecID,
    table=True
):
    __tablename__ = f"{prefix}_posts"
