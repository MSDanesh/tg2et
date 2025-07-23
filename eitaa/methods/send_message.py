from typing import TYPE_CHECKING, Optional

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_message import SendMessage as SendMessage_

from pyrogram.types.messages_and_media.message_entity import MessageEntity

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendMessage:
    async def send_message(
        self: "EitaaManager",
        chat: int,
        text: str,
        reply_to_message_id: Optional[int] = None,
        entities: Optional[list[MessageEntity]] = None,
    ):
        return await self.invoke(
            SendMessage_(
                peer=InputPeerChannel(
                    channel_id=abs(chat), access_hash=0
                ),
                message=text,
                random_id=self.rnd_id(),
                entities=self.make_entities(entities),
                reply_to_msg_id=reply_to_message_id,
                clear_draft=True
            )
        )