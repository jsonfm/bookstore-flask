#
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.models.base import CustomBaseModel


class User(CustomBaseModel):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    profile: Mapped["Profile"] = relationship(back_populates="user")


class Profile(CustomBaseModel):
    __tablename__ = "profiles"
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    user: Mapped["User"] = relationship(back_populates="profile")
