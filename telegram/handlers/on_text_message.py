from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnText(client: "TelegramManager", message: Message):
    await client.parent.et.send_message(
        message.chat.eitaa_id,
        message.text,
        message.reply_to_eitaa_message_id,
        message.entities
    )