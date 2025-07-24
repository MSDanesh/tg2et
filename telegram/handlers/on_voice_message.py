from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnVoice(client: "TelegramManager", message: Message):
    voice = await client.download_media(message.voice, in_memory=True)

    updates = await client.parent.et.send_voice(
        message.chat.eitaa_id,
        voice,
        voice.name,
        message.voice.duration,
        message.caption,
        message.voice.waveform,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.channel_id, message.id, et_message_id)