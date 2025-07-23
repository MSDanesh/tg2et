from pyrogram.types import Message
from pyrogram.enums import MessageServiceType
from pyrogram.filters import create, animation, audio, document, media_group, photo, sticker, text, video, video_note, voice


async def pin_filter(_, __, message: Message):
    return bool(message.service == MessageServiceType.PINNED_MESSAGE)

pin = create(pin_filter)


__all__ = ["animation", "audio", "document", "media_group", "photo", "pin", "sticker", "text", "video", "video_note", "voice"]