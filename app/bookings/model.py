from sqlalchemy import JSON, ForeignKey, Date, Computed, Integer
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base


class Bookings(Base):
    id:Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[Date] = mapped_column(Date)
    date_to: Mapped[Date] = mapped_column(Date)
    price:Mapped[int]
    total_cost:Mapped[int] = mapped_column(Integer,Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] =mapped_column(Integer, Computed("(date_to - date_from)"))