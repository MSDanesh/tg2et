from typing import TYPE_CHECKING

from pyrogram.types.messages_and_media.message import Message

from pyrogram.utils import MAX_CHANNEL_ID
from pyrogram.raw.types.input_channel import InputChannel
from pyrogram.raw.types.input_peer_channel import InputPeerChannel

if TYPE_CHECKING:
    from ..manager import TelegramManager


class AddChannel:
    async def add_channel(self: "TelegramManager", message: Message, params: list[str]):
        if len(params) != 2:
            return

        tg, et = params

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

        try:
            et_id = await self.parent.et.get_channel_id(
                int(et) if et.isdecimal() else et.removeprefix("@")
            )

            if not et_id:
                raise

        except:
            return await message.reply_text(f"Channel ({et}) not found in Eitaa.", quote=True)

        await self.parent.db.add_channel(MAX_CHANNEL_ID - tg_id, et_id)

        return await message.reply_text(f"Channels successfully added and paired.", quote=True)

