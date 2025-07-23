from typing import TYPE_CHECKING

from pyrogram.types import Message
from pyrogram.enums import MessageServiceType
from pyrogram.filters import create, animation, audio, document, media_group, photo, sticker, text, video, video_note, voice, enums

if TYPE_CHECKING:
    from .manager import TelegramManager

async def pin_filter(_, __, message: Message):
    return bool(message.service == MessageServiceType.PINNED_MESSAGE)

pin = create(pin_filter)


async def channel_filter(_, client: "TelegramManager", message: Message):
    if message.chat.type == enums.ChatType.CHANNEL:
        channel = await client.parent.db.get_channel(message.chat.id)

        if channel:
            if message.reply_to_message_id:
                message.reply_to_eitaa_message_id = await client.parent.db.get_post(
                    message.chat.id,
                    message.reply_to_message_id
                )

            else:
                message.reply_to_eitaa_message_id = None

            message.chat.eitaa_id = channel.et

            return True

    return False

channel = create(channel_filter)

__all__ = ["animation", "audio", "document", "media_group", "photo", "pin", "sticker", "text", "video", "video_note", "voice", "channel"]