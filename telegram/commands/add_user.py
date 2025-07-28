from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


class AddUser:
    async def add_user(self: "TelegramManager", message: Message, params: list[str]):
        if not params:
            return

        user = params[0]

        try:
            peer = await self.resolve_peer(
                int(user) if user.isdecimal() else user.removeprefix("@")
            )

        except:
            return await message.reply_text(f"User ({user}) not found.", quote=True)

        if user_id := getattr(peer, "user_id", None):
            await self.parent.db.add_user(user_id, user)

            return await message.reply_text(f"User `{user_id}`  ({user}) successfuly added.", quote=True)

        raise ValueError("Invalid peer %s" % peer)
            