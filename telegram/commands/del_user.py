from typing import TYPE_CHECKING
from pyrogram.types.messages_and_media.message import Message

if TYPE_CHECKING:
    from ..manager import TelegramManager


class DelUser:
    async def del_user(self: "TelegramManager", message: Message, params: list[str]):
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
            if user := await self.parent.db.get_user(user_id):
                if user.name == "admin":
                    return await message.reply_text(f"User `{user_id}` is the main admin, you can't do that.", quote=True)

                else:
                    await self.parent.db.delete_user(user_id)
                    return await message.reply_text(f"User `{user_id}`  ({user.name}) successfuly deleted.", quote=True)

            else:
                return await message.reply_text(f"User `{user_id}`  ({user}) doesn't exist.", quote=True)

        raise ValueError("Invalid peer %s" % peer)
            