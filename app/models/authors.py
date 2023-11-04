#
from sqlalchemy.orm import Mapped

from app.common.models.base import CustomBaseModel


class Author(CustomBaseModel):
    __tablename__ = "authors"
    name: Mapped[str]
    bio: Mapped[str]
