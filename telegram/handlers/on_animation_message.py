from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnAnimation(client: "TelegramManager", message: Message):
    animation = await client.download_media(message.animation, in_memory=True)

    updates = await client.parent.et.send_animation(
        message.chat.eitaa_id,
        animation,
        animation.name,
        message.animation.duration,
        message.animation.width,
        message.animation.height,
        message.caption,
        message.reply_to_eitaa_message_id,
        message.caption_entities
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.channel_id, message.id, et_message_id)