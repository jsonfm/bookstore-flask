# sqlalchemy
from sqlalchemy.orm import Mapped

# crud
from app.common.models.crud import CRUD

# types
from app.common.types.sqlalchemy import intpk, timestamp, timestamp_update

# database
from app.db import Base


class CommonFields(Base):
    """Common Fields for an SQLAlchemy Model."""

    __abstract__ = True
    id: Mapped[intpk]
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp_update]
    visible: Mapped[bool] = True
    deleted: Mapped[bool] = True


class CustomBaseModel(CommonFields, CRUD):
    """Custom Base SQLAlchemy model, with common crud operations and common fields."""

    __abstract__ = True
