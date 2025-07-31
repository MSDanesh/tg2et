from typing import TYPE_CHECKING, Optional

from pyeitaa.raw.types.input_channel import InputChannel
from pyeitaa.raw.functions.channels.get_full_channel import GetFullChannel
from pyeitaa.raw.functions.contacts.resolve_username import ResolveUsername

from pyeitaa.raw.types.peer_channel import PeerChannel
from pyeitaa.raw.types.channel_full import ChannelFull

if TYPE_CHECKING:
    from ..manager import EitaaManager


class GetChannelID:
    async def get_channel_id(
        self: "EitaaManager",
        chat: int | str,
    ) -> Optional[int]:
        match chat:
            case str():
                chat = await self.invoke(
                    ResolveUsername(
                        username=chat
                    )
                )

                if isinstance(chat.peer, PeerChannel):
                    return chat.peer.channel_id

            case int():
                chat = self.invoke(
                    GetFullChannel(
                        channel=InputChannel(channel_id=chat)
                    )
                )

                if isinstance(chat.full_chat, ChannelFull):
                    return chat.full_chat.id
