from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_document import InputMediaUploadedDocument
from pyeitaa.raw.types.document_attribute_filename import DocumentAttributeFilename

from pyeitaa.session_internals import DcType

from pyrogram.types.messages_and_media.message_entity import MessageEntity

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendDocument:
    async def send_document(
        self: "EitaaManager",
        chat: int,
        document: BytesIO,
        file_name: str,
        caption: str = "",
        reply_to_message_id: Optional[int] = None,
        entities: Optional[list[MessageEntity]] = None,
    ):
        file = await self.save_file(document, file_name)

        return await self.invoke(
            SendMedia(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type=self.guess_mime_type(file_name) or "application/zip",
                    attributes=[
                        DocumentAttributeFilename(file_name=file_name)
                    ]
                ),
                message=caption or "",
                random_id=self.rnd_id(),
                reply_to_msg_id=reply_to_message_id,
                entities=self.make_entities(entities),
                clear_draft=True
            ),
            dc_type=DcType.UPLOAD
        )