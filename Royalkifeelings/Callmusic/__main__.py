import asyncio
import importlib

from pytgcalls import idle

from Royalkifeelings.import BOT_USERNAME, bot, call_py
from Royalkifeelings.plugins import ALL_PLUGINS

loop = asyncio.get_event_loop()


async def Royalboyamit_boot():
    for all_module in ALL_PLUGINS:
        importlib.import_module("Royalkifeelings.plugins." + all_module)
    await bot.start()
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(Royalkifeelings_boot())
