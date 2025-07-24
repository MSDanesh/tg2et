from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnPin(client: "TelegramManager", message: Message):
    if message.reply_to_eitaa_message_id:
        updates = await client.parent.et.pin_message(
            message.chat.eitaa_id,
            message.reply_to_eitaa_message_id
        )

        for et_message_id in client.parent.et.get_message_id(updates):
            await client.parent.db.add_post(message.chat.channel_id, message.id, et_message_id)