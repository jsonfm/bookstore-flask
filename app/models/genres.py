#
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.models.base import CustomBaseModel


class Genre(CustomBaseModel):
    __tablename__ = "genres"
    name: Mapped[str]
    description: Mapped[Optional[str]]
    book: Mapped["Book"] = relationship(back_populates="genres")
