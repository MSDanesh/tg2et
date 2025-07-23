from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnDocument(client: "TelegramManager", message: Message):
    document = await client.download_media(message.document, in_memory=True)

    await client.parent.et.send_document(
        message.chat.eitaa_id,
        document,
        document.name,
        message.caption,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )