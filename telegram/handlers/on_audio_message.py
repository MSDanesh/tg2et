from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnAudio(client: "TelegramManager", message: Message):
    audio = await client.download_media(message.audio, in_memory=True)

    updates = await client.parent.et.send_audio(
        message.chat.eitaa_id,
        audio,
        audio.name,
        message.audio.duration,
        message.caption,
        message.audio.title,
        message.audio.performer,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.id, message.id, et_message_id)