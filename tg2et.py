from eitaa import EitaaManager
from telegram import TelegramManager
from database import Database

from sys import platform
from warnings import filterwarnings
from dotenv.main import dotenv_values

from pyrogram.methods.utilities.idle import idle

if platform != "win32":
    import uvloop # type: ignore
    uvloop.install()

filterwarnings("ignore")

env = dotenv_values()


class Tg2Et:
    def __init__(self):
        self.et = EitaaManager("et",
                               phone_number=env.get("ET_PHONE_NUMBER")
                               )
        self.tg = TelegramManager(self, "tg",
                                  api_id=env.get("TG_API_ID"),
                                  api_hash=env.get("TG_API_HASH"),
                                  bot_token=env.get("TG_BOT_TOKEN")
                                  )
        self.db = Database()

    async def run(self):
        await self.db.create_base()
        
        if admin_id := env.get("ADMIN_ID"):
            await self.db.add_user(admin_id, "admin")

        async with self.et, self.tg:
            await idle()
