from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_photo import InputMediaUploadedPhoto

from pyeitaa.session_internals import DcType

from pyrogram.types.messages_and_media.message_entity import MessageEntity

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendPhoto:
    async def send_photo(
        self: "EitaaManager",
        chat: int,
        photo: BytesIO,
        file_name: str,
        caption: str = "",
        reply_to_message_id: Optional[int] = None,
        entities: Optional[list[MessageEntity]] = None,
    ) -> None:
        file = await self.save_file(photo, file_name)

        return await self.invoke(
            SendMedia(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                media=InputMediaUploadedPhoto(file=file),
                message=caption or "",
                random_id=self.rnd_id(),
                entities=self.make_entities(entities),
                reply_to_msg_id=reply_to_message_id,
                clear_draft=True
            ),
            dc_type=DcType.UPLOAD
        )