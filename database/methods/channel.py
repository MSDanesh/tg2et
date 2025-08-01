from __future__ import annotations

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select, delete, or_

from typing import TYPE_CHECKING, Optional

from .base import use
from ..tables.channel import Channel

if TYPE_CHECKING:
    from .. import Database


class ChannelMethods:
    async def add_channel(self: Database, tg_id: int, et_id: int) -> Channel:
        channel = Channel(
            tg=tg_id,
            et=et_id,
        )

        try:
            async with use, self.session() as session:
                session.add(channel)
                await session.commit()

        except IntegrityError:
            pass

        return channel

    async def delete_channel(self: Database, channel_id: int) -> None:
        async with use, self.session() as session:
            await session.execute(
                delete(Channel)
                .where(Channel.id == channel_id)
            )
            await session.commit()

    async def get_channel(self: Database, tg_channel: int = None) -> Optional[Channel]:
        async with use, self.session() as session:
            result = await session.execute(
                select(Channel)
                .where(Channel.tg == tg_channel)
                .limit(1)
            )

            return result.scalar()

    async def get_channels(self: Database, offset: int = None, limit: int = None) -> list[Channel]:
        async with use, self.session() as session:
            result = await session.execute(
                select(Channel)
                .offset(offset)
                .limit(limit)
            )

            return result.scalars().all()