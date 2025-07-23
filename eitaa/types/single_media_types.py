from io import BytesIO
from dataclasses import dataclass

from pyrogram.types.messages_and_media.message_entity import MessageEntity


@dataclass
class InputPhoto:
    photo: BytesIO
    caption: str = ""
    entities: list[MessageEntity] = None

@dataclass
class InputVideo:
    video: BytesIO
    width: int
    height: int
    duration: int
    caption: str = ""
    entities: list[MessageEntity] = None
    supports_streaming: bool = True
    no_sound: bool = None
    thumb: BytesIO = None

@dataclass
class InputAudio:
    audio: BytesIO
    duration: int
    title: str = ""
    performer: str = ""
    caption: str = ""
    entities: list[MessageEntity] = None
    thumb: BytesIO = None

@dataclass
class InputDocument:
    document: BytesIO
    caption: str = ""
    entities: list[MessageEntity] = None
    thumb: BytesIO = None