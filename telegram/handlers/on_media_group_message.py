from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message
from pyrogram.enums.message_media_type import MessageMediaType

from eitaa.types import *

if TYPE_CHECKING:
    from ..manager import TelegramManager

from asyncio import Lock, sleep


lock = Lock()
messages = {}


async def OnMediaGroup(client: "TelegramManager", message: Message):
    async with lock: # you know, python isn’t quite fast enough to be counted on
        if message.media_group_id in messages:
            return messages[message.media_group_id].append(message)

    messages[message.media_group_id] = [message]

    await sleep(5) # wait 5s for other messages to be saved

    media = []

    for msg in messages.pop(message.media_group_id):
        match msg.media:
            case MessageMediaType.PHOTO:
                m = await client.download_media(msg.photo, in_memory=True)

                media.append(
                    InputPhoto(
                        m,
                        msg.caption,
                        msg.caption_entities
                    )
                )

            case MessageMediaType.VIDEO:
                m = await client.download_media(msg.video, in_memory=True)

                media.append(
                    InputVideo(
                        m,
                        msg.video.width,
                        msg.video.height,
                        msg.video.duration,
                        msg.caption,
                        msg.caption_entities,
                        msg.video.supports_streaming,
                    )
                )

            case MessageMediaType.AUDIO:
                m = await client.download_media(msg.audio, in_memory=True)

                media.append(
                    InputAudio(
                        m,
                        msg.audio.duration,
                        msg.audio.title,
                        msg.audio.performer,
                        msg.caption,
                        msg.caption_entities
                    )
                )

            case MessageMediaType.DOCUMENT:
                m = await client.download_media(msg.document, in_memory=True)

                media.append(
                    InputDocument(
                        m,
                        msg.caption,
                        msg.caption_entities
                    )
                )

    updates = await client.parent.et.send_media_group(
        message.chat.eitaa_id,
        media,
        message.reply_to_eitaa_message_id
    )

    for et_message_id in client.parent.et.get_message_id(updates):
        await client.parent.db.add_post(message.chat.channel_id, message.id, et_message_id)