import asyncio
import logging
import sys

from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from db import engine, User, Message

Session = sessionmaker(bind=engine)

session = Session()

load_dotenv('.env')

TOKEN = getenv('TOKEN')

dp = Dispatcher()

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id,
                message.from_user.username, str(message.date))
    session.add(user)
    session.commit()
    await message.answer('You`ve been added!!!')


@dp.message()
async def echo_handler(message: types.Message) -> None:
    if message.chat.id != '':
        chat_info = await bot.get_chat(message.chat.id)
        group_name = chat_info.title
        user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id,
                    message.from_user.username, str(message.date))
        message_text = Message(message.from_user.id, message.text, message.chat.id, group_name, str(message.date))
        session.add(user)
        session.commit()
        session.add(message_text)
        session.commit()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
