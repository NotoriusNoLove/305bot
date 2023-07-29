import pickle
from typing import Callable, Dict, Any, Awaitable, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


def on_startup():
    chat_id = {}
    try:
        chat_id = pickle.load(open('test_file', 'rb'))
    except:
        print("chat_id_list не найден")
    print(chat_id)
    return chat_id


chat_id = on_startup()


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


def on_shutdown():
    pickle.dump(chat_id, open('test_file', 'wb'))
