from sqlalchemy import JSON
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base


class Hotels(Base):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    location: Mapped[str]
    services: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
    room_quantity: Mapped[str]
    image_id: Mapped[int]


