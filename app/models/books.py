#
from typing import List

from sqlalchemy.orm import Mapped, relationship

from app.common.models.base import CustomBaseModel


class Book(CustomBaseModel):
    __tablename__ = "books"
    name: Mapped[str]
    description: Mapped[str]
    slug: Mapped[str]
    genres: Mapped[List["Genre"]] = relationship(back_populates="book")
    editorial: Mapped["Editorial"] = relationship(back_populates="book")
