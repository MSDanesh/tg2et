from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

from ..commands import Commands

if TYPE_CHECKING:
    from ..manager import TelegramManager


async def OnCommand(client: "TelegramManager", message: Message, prefix: str = "/"):
    if message.text is None or not message.text.startswith(prefix):
        return

    params = message.text.split()
    cmd = params.pop(0).removeprefix(prefix).lower()
    
    if hasattr(Commands, cmd):
        await getattr(client, cmd).__call__(message, params)