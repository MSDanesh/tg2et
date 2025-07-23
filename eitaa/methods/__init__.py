from .send_photo import SendPhoto
from .send_video import SendVideo
from .send_audio import SendAudio
from .send_voice import SendVoice
from .send_message import SendMessage
from .send_sticker import SendSticker
from .send_document import SendDocument
from .send_animation import SendAnimation
from .send_video_note import SendVideoNote
from .send_media_group import SendMediaGroup

from .pin_message import PinMessage
from .unpin_message import UnpinMessage
from .unpin_all_messages import UnpinAllMessages

from .edit_message import EditMessage
from .delete_message import DeleteMessage

class Methods(
    SendPhoto,
    SendVideo,
    SendAudio,
    SendVoice,
    SendMessage,
    SendSticker,
    SendDocument,
    SendAnimation,
    SendVideoNote,
    SendMediaGroup,

    PinMessage,
    UnpinMessage,
    UnpinAllMessages,

    EditMessage,
    DeleteMessage,

):
    ...