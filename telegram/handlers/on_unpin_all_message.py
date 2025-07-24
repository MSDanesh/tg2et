from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnUnpinAll(client: "TelegramManager", message: Message):
    return NotImplemented