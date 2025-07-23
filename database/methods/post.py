from __future__ import annotations

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select, delete, desc, and_

from typing import TYPE_CHECKING, Optional

from .base import use
from ..tables.post import Post

if TYPE_CHECKING:
    from .. import Database


class PostMethods:
    async def add_post(self: Database, tg_channel: int, tg_post_id: int, et_post_id: int) -> Post:
        post = Post(
            tg=tg_channel,
            tg_id=tg_post_id,
            et_id=et_post_id,
        )

        try:
            async with use, self.session() as session:
                session.add(post)
                await session.commit()

        except IntegrityError:
            pass

        return post

    async def delete_post(self: Database, tg_channel: int, tg_post_id: int) -> None:
        async with use, self.session() as session:
            await session.execute(
                delete(Post)
                .where(
                    and_(Post.tg == tg_channel, Post.tg_id == tg_post_id)
                )
            )

            await session.commit()

    async def get_post(self: Database, tg_channel: int, tg_post_id: int) -> Optional[Post]:
        async with use, self.session() as session:
            result = await session.execute(
                select(Post)
                .where(
                    and_(Post.tg == tg_channel, Post.tg_id == tg_post_id)
                )
                .limit(1)
            )

            return result.scalar()

    async def get_channel_posts(self: Database, tg_channel: int, offset: int = None, limit: int = None) -> list[Post]:
        async with use, self.session() as session:
            result = await session.execute(
                select(Post)
                .order_by(desc(Post.tg_id))
                .where(Post.tg == tg_channel)
                .offset(offset)
                .limit(limit)
            )

            return result.scalars().all()
