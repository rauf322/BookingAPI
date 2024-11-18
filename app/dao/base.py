from datetime import date

from sqlalchemy import select, insert, and_, or_, func, delete

import app.bookings.model
from app.database import async_session_maker
from app.bookings.model import Bookings
from app.rooms.models import Rooms


#Abstract class that we implement for other models by using staticmethod can do the same with classmethod
#But by using staticmethod we make it more flexible and prevent ourselves to mutate model variable in class object
class BaseDAO:

    #Find the something by id
    @staticmethod
    async def find_by_id(model, model_id:int):
        async with async_session_maker() as session:
            query = select(model).filter_by(id = model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    #can find something by using multiple arguments but return only one or none object
    @staticmethod
    async def find_one_or_none(model, **filter_by):
        async with async_session_maker() as session:
            query = select(model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    #Return all if property wasn't sent, working like filter of public elements not private
    @staticmethod
    async def find_all_hotels(model, **filter_by):
        async with async_session_maker() as session:
            query = select(model)
            #Optional for Hotels
            if 'id' in filter_by and filter_by['id']:
                query = select(model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    # Return multiple objects by searching on multiple properties
    @staticmethod
    async def find_all(model, **filter_by):
        async with async_session_maker() as session:
            query = select(model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def add(model, **data):
        async with async_session_maker() as session:
            query = insert(model).values(**data)
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def add_booking(user_id:int,
                          room_id:int,
                          date_from: date,
                          date_to:date,
                          model = Bookings):
        async with async_session_maker() as session:
            cte = select(Bookings).where(and_(
                Bookings.room_id == room_id,
                and_(
                    Bookings.date_from <= date_from, Bookings.date_to >= date_to
                )
            )).cte("booked_rooms")
            query = select(Rooms.quantity - func.count(cte.c.room_id)).select_from(Rooms).outerjoin(cte,
                cte.c.room_id == Rooms.id).where(Rooms.id == room_id).group_by(Rooms.quantity)
            res = await session.execute(query)
            result = res.scalar()
            if result > 0:
                get_price = select(Rooms.price).where(Rooms.id == room_id)
                price = await session.execute(get_price)
                price:int = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(Bookings)
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None

    @staticmethod
    async def delete_booking(model, user_id:int):
        async with async_session_maker() as session:
            query = select(model).filter_by(user_id = user_id)
            result = await session.execute(query)
            delete_row = result.scalars().all()
            if not delete_row:
                return "No bookings found for the given user"
            query = delete(model).filter_by(user_id=user_id)
            result = await session.execute(query)
            await session.commit()
            return delete_row