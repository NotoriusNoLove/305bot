from typing import Callable, Dict, Any, Awaitable, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from dispatcher import bot
import pickle
from way import chat_id


async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f'notmeowmeow.ru/bot/305bot', drop_pending_updates=True)


class RegisterCheck(BaseMiddleware):
    """
    Middleware будет вызываться каждый раз, когда пользователь будет отправлять боту сообщения (или нажимать
    на кнопку в инлайн-клавиатуре).
    """

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        if event.chat.id in chat_id:
            pass
        else:
            if event.chat.id < 0:
                chat_id[event.chat.id] = 0
            else:
                chat_id[event.chat.id] = 0
        return await handler(event, data)


async def on_shutdown():
    pickle.dump(chat_id, open('test_file', 'wb'))
    await bot.delete_webhook(drop_pending_updates=True)
