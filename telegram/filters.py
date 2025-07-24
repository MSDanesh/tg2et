from typing import TYPE_CHECKING

from pyrogram.types import Message
from pyrogram.filters import create, animation, audio, document, media_group, photo, sticker, text, video, video_note, voice, pinned_message as pin, enums

if TYPE_CHECKING:
    from .manager import TelegramManager


async def channel_filter(_, client: "TelegramManager", message: Message):
    if message.chat.type == enums.ChatType.CHANNEL:
        channel = await client.parent.db.get_channel(message.chat.id)

        if channel:
            if message.reply_to_message_id or message.pinned_message:
                message.reply_to_eitaa_message_id = await client.parent.db.get_post(
                    channel.id,
                    message.pinned_message.id if message.pinned_message else message.reply_to_message_id
                )

                if message.reply_to_eitaa_message_id:
                    message.reply_to_eitaa_message_id = message.reply_to_eitaa_message_id.et_id

            else:
                message.reply_to_eitaa_message_id = None

            message.chat.eitaa_id = channel.et
            message.chat.channel_id = channel.id

            return True

    return False

channel = create(channel_filter)


async def message_filter(_, client: "TelegramManager", message: Message):
    if message.chat.type == enums.ChatType.CHANNEL:
        channel = await client.parent.db.get_channel(message.chat.id)

        if channel:
            message.eitaa_message_id = await client.parent.db.get_post(
                channel.id, message.id
            )

            if message.eitaa_message_id:
                message.chat.eitaa_id = channel.et
                message.eitaa_message_id = message.eitaa_message_id.et_id

                return True

    return False

message = create(message_filter)

__all__ = ["animation", "audio", "document", "media_group", "photo", "pin", "sticker", "text", "video", "video_note", "voice", "channel", "message"]