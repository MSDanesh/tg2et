from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_photo import InputMediaUploadedPhoto
from pyeitaa.raw.types.input_single_media import InputSingleMedia
from pyeitaa.raw.types.input_media_photo import InputMediaPhoto
from pyeitaa.raw.types.input_media_document import InputMediaDocument
from pyeitaa.raw.types.input_media_uploaded_document import InputMediaUploadedDocument
from pyeitaa.raw.types.document_attribute_filename import DocumentAttributeFilename
from pyeitaa.raw.types.document_attribute_video import DocumentAttributeVideo
from pyeitaa.raw.types.document_attribute_audio import DocumentAttributeAudio
from pyeitaa.raw.types.input_photo import InputPhoto as InputPhoto_
from pyeitaa.raw.types.input_document import InputDocument as InputDocument_

from pyeitaa.raw.functions.messages.upload_media import UploadMedia
from pyeitaa.raw.functions.messages.send_multi_media import SendMultiMedia

from pyeitaa.session_internals import DcType

from ..types.single_media_types import InputPhoto, InputVideo, InputAudio, InputDocument

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendMediaGroup:
    async def send_media_group(
        self: "EitaaManager",
        chat: int,
        media: list[InputPhoto | InputVideo | InputAudio | InputDocument],
        reply_to_message_id: Optional[int] = None,
    ) -> None:
        multi_media = []

        peer = InputPeerChannel(
            channel_id=chat, access_hash=0
        )

        for m in media:
            match m:
                case InputPhoto():
                    uploaded_media = await self.invoke(
                        UploadMedia(
                            peer=peer,
                            media=InputMediaUploadedPhoto(
                                file=await self.save_file(m.photo, m.photo.name or "photo.jpg")
                            )
                        ),
                        dc_type=DcType.UPLOAD
                    )

                    final_media = InputMediaPhoto(
                        id=InputPhoto_(
                            id=uploaded_media.photo.id,
                            access_hash=uploaded_media.photo.access_hash,
                            file_reference=uploaded_media.photo.file_reference
                        )
                    )

                case InputVideo():
                    uploaded_media = await self.invoke(
                        UploadMedia(
                            peer=peer,
                            media=InputMediaUploadedDocument(
                                mime_type=self.guess_mime_type(m.video.name) or "video/mp4",
                                file=await self.save_file(m.video, m.video.name or "video.mp4"),
                                attributes=[
                                    DocumentAttributeVideo(
                                        supports_streaming=m.supports_streaming or None,
                                        duration=m.duration,
                                        w=m.width,
                                        h=m.height
                                    ),
                                    DocumentAttributeFilename(
                                        file_name=m.video.name or "video.mp4"
                                    )
                                ]
                            )
                        ),
                        dc_type=DcType.UPLOAD
                    )

                    final_media = InputMediaDocument(
                        id=InputDocument_(
                            id=uploaded_media.document.id,
                            access_hash=uploaded_media.document.access_hash,
                            file_reference=uploaded_media.document.file_reference
                        )
                    )

                case InputAudio():
                    uploaded_media = await self.invoke(
                        UploadMedia(
                            peer=peer,
                            media=InputMediaUploadedDocument(
                                mime_type=self.guess_mime_type(m.audio.name) or "audio/mpeg",
                                file=await self.save_file(m.audio, m.audio.name or "audio.mp3"),
                                attributes=[
                                    DocumentAttributeAudio(
                                        duration=m.duration,
                                        title=m.title,
                                        performer=m.performer
                                    ),
                                    DocumentAttributeFilename(
                                        file_name=m.audio.name or "audio.mp3"
                                    )
                                ]
                            )
                        ),
                        dc_type=DcType.UPLOAD
                    )

                    final_media = InputMediaDocument(
                        id=InputDocument_(
                            id=uploaded_media.document.id,
                            access_hash=uploaded_media.document.access_hash,
                            file_reference=uploaded_media.document.file_reference
                        )
                    )

                case InputDocument():
                    uploaded_media = await self.invoke(
                        UploadMedia(
                            peer=peer,
                            media=InputMediaUploadedDocument(
                                mime_type=self.guess_mime_type(m.document.name) or "application/zip",
                                file=await self.save_file(m.document, m.document.name or "doc.zip"),
                                attributes=[
                                    DocumentAttributeFilename(
                                        file_name=m.document.name or "doc.zip"
                                    )
                                ]
                            )
                        ),
                        dc_type=DcType.UPLOAD
                    )

                    final_media = InputMediaDocument(
                        id=InputDocument_(
                            id=uploaded_media.document.id,
                            access_hash=uploaded_media.document.access_hash,
                            file_reference=uploaded_media.document.file_reference
                        )
                    )

                case _:
                    raise TypeError(m)

            multi_media.append(
                InputSingleMedia(
                    media=final_media,
                    random_id=self.rnd_id(),
                    message=m.caption or "",
                    entities=self.make_entities(m.entities)
                )
            )

        return await self.invoke(
            SendMultiMedia(
                peer=peer,
                multi_media=multi_media,
                clear_draft=True,
                reply_to_msg_id=reply_to_message_id
            ),
            dc_type=DcType.UPLOAD
        )