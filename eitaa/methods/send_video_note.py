from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_document import InputMediaUploadedDocument
from pyeitaa.raw.types.document_attribute_video import DocumentAttributeVideo

from pyeitaa.session_internals import DcType

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendVideoNote:
    async def send_video_note(
        self: "EitaaManager",
        chat: int,
        video_note: BytesIO,
        file_name: str,
        duration: int,
        length: int,
        reply_to_message_id: Optional[int] = None,
    ):
        file = await self.save_file(video_note, file_name)

        return await self.invoke(
            SendMedia(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type=self.guess_mime_type(file_name) or "video/mp4",
                    attributes=[
                        DocumentAttributeVideo(
                            round_message=True,
                            duration=duration,
                            w=length,
                            h=length
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