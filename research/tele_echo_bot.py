import logging
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
logging(API_TOKEN)

#configuretion logging
logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start`  or '/help'command
    """
    
    await message.reply(f"Hello\n I am Hammer Bot ready for scrapping !!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)