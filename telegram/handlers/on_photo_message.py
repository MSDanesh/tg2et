from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnPhoto(client: "TelegramManager", message: Message):
    photo = await client.download_media(message.photo, in_memory=True)

    updates = await client.parent.et.send_photo(
        message.chat.eitaa_id,
        photo,
        photo.name,
        message.caption,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.id, message.id, et_message_id)