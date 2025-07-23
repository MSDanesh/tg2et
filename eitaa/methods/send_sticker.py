from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_document import InputMediaUploadedDocument
from pyeitaa.raw.types.document_attribute_filename import DocumentAttributeFilename
from pyeitaa.raw.types.document_attribute_sticker import DocumentAttributeSticker
from pyeitaa.raw.types.input_sticker_set_empty import InputStickerSetEmpty

from pyeitaa.session_internals import DcType

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendSticker:
    async def send_sticker(
        self: "EitaaManager",
        chat: int,
        sticker: BytesIO,
        file_name: str,
        emoji: str,
        reply_to_message_id: Optional[int] = None,
    ) -> None:
        file = await self.save_file(sticker, file_name)

        return await self.invoke(
            SendMedia(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type=self.guess_mime_type(file_name) or "image/webp",
                    attributes=[
                        DocumentAttributeFilename(file_name=file_name),
                        DocumentAttributeSticker(
                            alt=emoji,
                            stickerset=InputStickerSetEmpty()
                        )
                    ]
                ),
                message="",
                random_id=self.rnd_id(),
                reply_to_msg_id=reply_to_message_id,
                clear_draft=True
            ),
            dc_type=DcType.UPLOAD
        )