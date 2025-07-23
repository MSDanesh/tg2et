from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnPhoto(client: "TelegramManager", message: Message):
    photo = await client.download_media(message.photo, in_memory=True)

    await client.parent.et.send_photo(
        message.chat.eitaa_id,
        photo,
        photo.name,
        message.caption,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )