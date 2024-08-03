from aiogram import Bot, Dispatcher
import asyncio
import os

from utils.handlers import router


async def main():
    bot = Bot(token=os.getenv("Betta_Token"))
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())