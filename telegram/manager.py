from typing import TYPE_CHECKING

from pyrogram.client import Client
from pyrogram.handlers import MessageHandler, EditedMessageHandler, DeletedMessagesHandler

from .filters import *
from .handlers import *
from .commands import Commands

if TYPE_CHECKING:
    from ..tg2et import Tg2Et


class TelegramManager(Client, Commands):
    def __init__(self, parent: "Tg2Et", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent = parent

        self.add_handler(MessageHandler(OnPin, pin & channel))
        self.add_handler(MessageHandler(OnText, text & channel))
        self.add_handler(MessageHandler(OnMediaGroup, media_group & channel))
        self.add_handler(MessageHandler(OnAnimation, animation & channel))
        self.add_handler(MessageHandler(OnAudio, audio & channel))
        self.add_handler(MessageHandler(OnDocument, document & channel))
        self.add_handler(MessageHandler(OnPhoto, photo & channel))
        self.add_handler(MessageHandler(OnSticker, sticker & channel))
        self.add_handler(MessageHandler(OnVideo, video & channel))
        self.add_handler(MessageHandler(OnVideoNote, video_note & channel))
        self.add_handler(MessageHandler(OnVoice, voice & channel))

        self.add_handler(MessageHandler(OnCommand, user))

        self.add_handler(EditedMessageHandler(OnEdit, message))
        self.add_handler(DeletedMessagesHandler(OnDelete))
