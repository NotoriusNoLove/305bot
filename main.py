from dispatcher import dp, bot
from hendlers import register_handlers
from middleware import on_shutdown, on_startup
from aiohttp.web import run_app
from aiohttp.web_app import Application
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


def main():
    register_handlers()
    dp.shutdown.register(on_shutdown)
    dp.startup.register(on_startup)
    dp['base_url'] = "notmeowmeow.ru"

    app = Application()
    app["bot"] = bot

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path="/bot/305bot")
    setup_application(app, dp, bot=bot)

    run_app(app, host="127.0.0.1", port=8003)


if __name__ == '__main__':
    main()
