from __future__ import annotations

from sqlalchemy.future import select
from sqlalchemy.sql.dml import Delete
from sqlalchemy.exc import IntegrityError

from typing import TYPE_CHECKING

from .base import use
from ..tables.user import User

if TYPE_CHECKING:
    from .. import Database


class UserMethods:
    async def add_user(self: Database, user_id: int, user_name: str) -> User:
        user = User(
            id=user_id,
            name=user_name
        )

        try:
            async with use, self.session() as session:
                session.add(user)
                await session.commit()

        except IntegrityError:
            pass

        return user

    async def delete_user(self: Database, user_id: int) -> None:
        async with use, self.session() as session:
            await session.execute(
                Delete(User)
                .where(User.id == user_id)
            )

            await session.commit()

    async def user_exists(self: Database, user_id: int) -> bool:
        async with use, self.session() as session:
            result = await session.execute(
                select(User.id)
                .where(User.id == user_id)
                .limit(1)
            )

            return bool(result.scalar())

    async def get_users(self: Database, offset: int = 0, limit: int = 20) -> list[User]:
        async with use, self.session() as session:
            result = await session.execute(
                select(User)
                .offset(offset)
                .limit(limit)
            )

            return result.scalars().all()
