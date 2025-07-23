from typing import TYPE_CHECKING, Optional

from io import BytesIO

from pyeitaa.raw.types.input_peer_channel import InputPeerChannel
from pyeitaa.raw.functions.messages.send_media import SendMedia
from pyeitaa.raw.types.input_media_uploaded_document import InputMediaUploadedDocument
from pyeitaa.raw.types.document_attribute_audio import DocumentAttributeAudio

from pyeitaa.session_internals import DcType

from pyrogram.types.messages_and_media.message_entity import MessageEntity

if TYPE_CHECKING:
    from ..manager import EitaaManager


class SendVoice:
    async def send_voice(
        self: "EitaaManager",
        chat: int,
        voice: BytesIO,
        file_name: str,
        duration: int,
        caption: str = "",
        waveform: Optional[bytes] = None,
        reply_to_message_id: Optional[int] = None,
        entities: Optional[list[MessageEntity]] = None,
    ):
        file = await self.save_file(voice, file_name)

        mime_type = self.guess_mime_type(file_name) or "audio/ogg"

        if mime_type == "audio/mpeg":
            mime_type = "audio/ogg"

        return await self.invoke(
            SendMedia(
                peer=InputPeerChannel(
                    channel_id=chat, access_hash=0
                ),
                media=InputMediaUploadedDocument(
                    file=file,
                    mime_type=mime_type,
                    attributes=[
                        DocumentAttributeAudio(
                            duration=duration,
                            voice=True,
                            waveform=waveform
                        )
                    ]
                ),
                message=caption or "",
                random_id=self.rnd_id(),
                entities=self.make_entities(entities),
                reply_to_msg_id=reply_to_message_id,
                clear_draft=True
            ),
            dc_type=DcType.UPLOAD
        )