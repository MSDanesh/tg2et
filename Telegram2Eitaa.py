from asyncio import get_event_loop
from tg2et import Tg2Et


async def main():
    copier = Tg2Et()
    await copier.run()


if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(main())
    loop.stop()