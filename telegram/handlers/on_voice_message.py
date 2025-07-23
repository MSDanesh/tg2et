from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnVoice(client: "TelegramManager", message: Message):
    voice = await client.download_media(message.voice, in_memory=True)

    await client.parent.et.send_voice(
        message.chat.eitaa_id,
        voice,
        voice.name,
        message.voice.duration,
        message.caption,
        message.voice.waveform,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )