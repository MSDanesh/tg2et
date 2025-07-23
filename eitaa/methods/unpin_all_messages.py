from typing import TYPE_CHECKING

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.unpin_all_messages import UnpinAllMessages as UnpinAllMessages_

if TYPE_CHECKING:
    from ..manager import EitaaManager


class UnpinAllMessages:
    async def unpin_all_messages(
        self: "EitaaManager",
        chat: int,
    ):
        return await self.invoke(
            UnpinAllMessages_(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                )
            )
        )