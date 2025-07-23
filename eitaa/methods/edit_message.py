from typing import TYPE_CHECKING, Optional

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.edit_message import EditMessage as EditMessage_

from pyrogram.types.messages_and_media.message_entity import MessageEntity

if TYPE_CHECKING:
    from ..manager import EitaaManager


class EditMessage:
    async def edit_message(
        self: "EitaaManager",
        chat: int,
        message_id: int,
        text: str,
        entities: Optional[list[MessageEntity]] = None,
    ) -> None:
        return await self.invoke(
            EditMessage_(
                peer=InputPeerChannel(
                    channel_id=abs(chat), access_hash=0
                ),
                id=message_id,
                message=text,
                entities=self.make_entities(entities)
            )
        )