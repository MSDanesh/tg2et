from typing import TYPE_CHECKING

from pyeitaa.raw.types.input_channel import InputChannel
from pyeitaa.raw.functions.channels.delete_messages import DeleteMessages

if TYPE_CHECKING:
    from ..manager import EitaaManager


class DeleteMessage:
    async def delete_message(
        self: "EitaaManager",
        chat: int,
        message_id: int
    ):
        return await self.invoke(
            DeleteMessages(
                channel=InputChannel(
                    channel_id=chat, access_hash=0
                ),
                id=[message_id]
            )
        )