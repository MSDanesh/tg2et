from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnSticker(client: "TelegramManager", message: Message):
    if message.sticker.is_animated or message.sticker.is_video:
        return

    sticker = await client.download_media(message.sticker, in_memory=True)

    await client.parent.et.send_sticker(
        message.chat.eitaa_id,
        sticker,
        sticker.name,
        message.sticker.emoji,
        message.reply_to_eitaa_message_id
    )