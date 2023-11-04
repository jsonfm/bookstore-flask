#
from sqlalchemy.orm import Mapped

from app.common.models.base import CustomBaseModel


class Editorial(CustomBaseModel):
    __tablename__ = "editorials"
    name: Mapped[str]
    description: Mapped[str]
