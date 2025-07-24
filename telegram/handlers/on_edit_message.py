from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message
from pyeitaa.errors.exceptions.bad_request_400 import MessageNotModified

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnEdit(client: "TelegramManager", message: Message):
    text = message.text or message.caption or ""

    try:
        await client.parent.et.edit_message(
            message.chat.eitaa_id,
            message.eitaa_message_id,
            text,
            message.entities or message.caption_entities
        )

    except MessageNotModified:
        pass