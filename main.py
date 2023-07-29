import asyncio
from dispatcher import dp, bot
from hendlers import register_handlers
from middleware import chat_id, on_shutdown, on_startup


async def main():
    register_handlers()
    dp.shutdown.register(on_shutdown)
    dp.startup.register(on_startup)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
