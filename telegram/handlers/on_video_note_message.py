from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnVideoNote(client: "TelegramManager", message: Message):
    video_note = await client.download_media(message.video_note, in_memory=True)

    updates = await client.parent.et.send_video_note(
        message.chat.eitaa_id,
        video_note,
        video_note.name,
        message.video_note.duration,
        message.video_note.length,
        message.reply_to_eitaa_message_id,
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.channel_id, message.id, et_message_id)