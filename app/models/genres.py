#
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.common.models.base import CustomBaseModel


class Genre(CustomBaseModel):
    __tablename__ = "genres"
    name: Mapped[str]
    description: Mapped[str]
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
