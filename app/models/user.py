#
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.models.base import CustomBaseModel


class User(CustomBaseModel):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    profile: Mapped["Profile"] = relationship(back_populates="user")
    role: Mapped["Role"] = relationship(back_populates="")


class Profile(CustomBaseModel):
    __tablename__ = "profiles"
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    user: Mapped["User"] = relationship(back_populates="profile")


class Role(CustomBaseModel):
    __tablename__ = "user_roles"
    role: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    user: Mapped["User"] = relationship(back_populates="role")
