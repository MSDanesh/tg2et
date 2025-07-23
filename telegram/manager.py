from pyrogram.client import Client
from pyrogram.handlers import MessageHandler, EditedMessageHandler, DeletedMessagesHandler

from .filters import *
from .handlers import *

class TelegramManager(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_handler(MessageHandler(OnPin, pin))
        self.add_handler(MessageHandler(OnText, text))
        self.add_handler(MessageHandler(OnMediaGroup, media_group))
        self.add_handler(MessageHandler(OnAnimation, animation))
        self.add_handler(MessageHandler(OnAudio, audio))
        self.add_handler(MessageHandler(OnDocument, document))
        self.add_handler(MessageHandler(OnPhoto, photo))
        self.add_handler(MessageHandler(OnSticker, sticker))
        self.add_handler(MessageHandler(OnVideo, video))
        self.add_handler(MessageHandler(OnVideoNote, video_note))
        self.add_handler(MessageHandler(OnVoice, voice))

        self.add_handler(EditedMessageHandler(OnEdit))
        self.add_handler(DeletedMessagesHandler(OnDelete))
