from typing import TYPE_CHECKING, Optional

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.update_pinned_message import UpdatePinnedMessage

if TYPE_CHECKING:
    from ..manager import EitaaManager


class PinMessage:
    async def pin_message(
        self: "EitaaManager",
        chat: int,
        message_id: int,
        silent: Optional[bool] = None
    ):
        return await self.invoke(
            UpdatePinnedMessage(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                id=message_id,
                silent=silent or None
            )
        )