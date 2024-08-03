from aiogram import Bot, Dispatcher
import asyncio
import os

from utils.handlers import router
from utils.stay_a_live import stay_a_live


async def main():
    bot = Bot(token=os.getenv("Betta_Token"))
    dp = Dispatcher()
    dp.include_router(router)
    stay_a_live()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
