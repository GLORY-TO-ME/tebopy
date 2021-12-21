from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
import time

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await message.answer('Тебон на связи, чего желаете? (функционал-рандомайзер)')
    await message.answer('(работоспособность с центиллионами не гарантирована)')


@dp.message_handler(commands=['help'])
async def command_help(message : types.Message):
    await message.answer('Я знаю следующие команды:')
    await message.answer('start - начальная команда')
    await message.answer('help - комманда помощи')
    await message.answer('randomNumber - случайное число')
    await message.answer('randomNumber+ - случайное число больше 0')
    await message.answer('цифра - диапозон для случайных чисел от нуля')


@dp.message_handler(commands=['randomNumber'])
async def command_number(message : types.Message):
    ran_num1=randint(-370000,370000)
    ran_num2=randint(-25000,25000)
    ran_num3=randint(-1000, 1000)
    temp_ran_num=randint(1,3)
    if temp_ran_num==1:
        ran_num = ran_num1
    elif temp_ran_num==2:
        ran_num = ran_num2
    elif temp_ran_num==3:
        ran_num = ran_num3
    await bot.send_message(message.from_user.id, ran_num)


@dp.message_handler(commands=['randomNumber+'])
async def command_number(message : types.Message):
    ran_num1=randint(0,370000)
    ran_num2=randint(0,25000)
    ran_num3=randint(0, 1000)
    temp_ran_num=randint(1,3)
    if temp_ran_num==1:
        ran_num = ran_num1
    elif temp_ran_num==2:
        ran_num = ran_num2
    elif temp_ran_num==3:
        ran_num = ran_num3
    await bot.send_message(message.from_user.id, ran_num)


@dp.message_handler(lambda message: message.text.isdigit())
async def command_number(message : types.Message()):
    range_num=int(message.text)
    range_num1=randint(0,range_num)
    await bot.send_message(message.from_user.id, range_num1)


@dp.message_handler()
async def echo_send(message : types.Message):
        await message.answer('Прошу простить меня за мою глупость, я не осведомлён о данных коммандах. Введите /help для получения списка доступных мне команд')

executor.start_polling(dp, skip_updates=True)

#help1 = 'choose lenguage | выберете язык'
#help2 = 'choose lenguage | выберете язык'
#help3 = 'choose lenguage | выберете язык'
#help4 = 'choose lenguage | выберете язык'
#help5 = 'choose lenguage | выберете язык'
#help6 = 'choose lenguage | выберете язык'
#startTXT = 'choose lenguage | выберете язык'
#helpTXT = 'choose lenguage | выберете язык'
#
#
#class Russian:
#    help1 = help1ru = 'Я знаю следующие команды:'
#    help2 = help2ru = 'start - начальная команда'
#    help3 = help3ru = 'help - комманда помощи'
#    help4 = help4ru = 'randomNumber - случайное число'
#    help5 = help5ru = 'randomNumber+ - случайное число больше 0'
#    help6 = help6ru = 'цифра - диапозон для случайных чисел от нуля'
#    startTXT = startRu = 'Тебон на связи, чего желаете? (функционал-рандомайзер)'
#    helpTXT = helpRU = 'Прошу простить меня за мою глупость, я не осведомлён о данных коммандах. Введите /help для получения списка доступных мне команд'
#
#
#class English:
#    help1 = help1en = 'Available commands:'
#    help2 = help2en = 'start - start command'
#    help3 = help3en = 'help - help command'
#    help4 = help4en = 'randomNumber - random number'
#    help5 = help5en = 'randomNumber+ - random number more than 0 '
#    help6 = help6en = 'digit - range of random numbers from zero'
#    startTXT = startEn = 'Hello i am Tebone! (bot-randomizer)'
#    helpTXT = helpEN = 'I beg your pardon for my stupidity, I am not aware of these commands. Enter / help for a list of commands available to me'
#
#
#@dp.message_handler(commands=['/en'])
#async def location(message: types.Message):
#
#
#@dp.message_handler(commands=['/ru'])
#async def location(message: types.Message):
