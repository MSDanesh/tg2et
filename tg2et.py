from eitaa import EitaaManager
from telegram import TelegramManager

from sys import platform
from dotenv.main import DotEnv
from os.path import dirname, join
from warnings import filterwarnings

from pyrogram.methods.utilities.idle import idle

if platform != "win32":
    import uvloop # type: ignore
    uvloop.install()

filterwarnings("ignore")

env = DotEnv(
    join(dirname(__file__), ".env"), override=True
)

env.set_as_environment_variables()


class Tg2Et:
    def __init__(self):
        self.et = EitaaManager("et",
                               phone_number=env.get("ET_PHONE_NUMBER")
                               )
        self.tg = TelegramManager("tg",
                                  api_id=env.get("TG_API_ID"),
                                  api_hash=env.get("TG_API_HASH"),
                                  bot_token=env.get("TG_BOT_TOKEN")
                                  )

    async def run(self):
        async with self.et, self.tg:
            await idle()
