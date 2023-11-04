#
from sqlalchemy.orm import Mapped, relationship

from app.common.models.base import CustomBaseModel


class Review(CustomBaseModel):
    __tablename__ = "reviews"
    stars: Mapped[int]
    book: Mapped["Book"] = relationship(back_populates="book")
