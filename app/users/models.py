from sqlalchemy import JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base


class Users(Base):
    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str]
    hashed_password: Mapped[str]