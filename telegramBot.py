from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
TOKEN = '5429668333:AAFZ1nZEThvZ2Nn9OCBUtzT2Gy2qx9KPneU'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    #await message.reply(message.text)




executor.start_polling(dp, skip_updates=True)