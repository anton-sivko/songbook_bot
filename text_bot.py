from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config_data.config import Config, load_config

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')

dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='<ins><i>Пример форматированного текста</i></ins>')


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)
