from sqlalchemy import JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base


class Rooms(Base):
    id:Mapped[int] = mapped_column(primary_key=True)
    hotel_id:Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name:Mapped[str]
    description:Mapped[str]
    price:Mapped[int]
    services: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
    quantity:Mapped[int]
    image_id: Mapped[int]