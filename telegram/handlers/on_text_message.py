from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnText(client: "TelegramManager", message: Message):
    updates = await client.parent.et.send_message(
        message.chat.eitaa_id,
        message.text,
        message.reply_to_eitaa_message_id,
        message.entities
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.id, message.id, et_message_id)
