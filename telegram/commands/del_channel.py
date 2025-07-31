from typing import TYPE_CHECKING

from pyrogram.types.messages_and_media.message import Message

from pyrogram.utils import MAX_CHANNEL_ID
from pyrogram.raw.types.input_channel import InputChannel
from pyrogram.raw.types.input_peer_channel import InputPeerChannel

if TYPE_CHECKING:
    from ..manager import TelegramManager


class DelChannel:
    async def del_channel(self: "TelegramManager", message: Message, params: list[str]):
        if not params:
            return

        tg = params[0]

        try:
            tg_peer = await self.resolve_peer(
                int(tg) if tg.isdecimal() else tg.removeprefix("@")
            )

            if isinstance(tg_peer, (InputPeerChannel, InputChannel)):
                tg_id = tg_peer.channel_id

            else:
                raise

        except:
            return await message.reply_text(f"Channel ({tg}) not found in Telegram.", quote=True)

        if channel := await self.parent.db.get_channel(MAX_CHANNEL_ID - tg_id):
            await self.parent.db.delete_channel(channel.id)

        else:
            return await message.reply_text(f"Telegram channel ({tg}) doesn't exist.", quote=True)

        return await message.reply_text(f"Channel ({tg}) successfully deleted.", quote=True)

