from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
temp = ""
members = list()
locs = ['Бонч', 'Аквапарк', 'Цирк', 'Подводная лодка', 'Космическая станция']

async def on_startup(_):
	print('Started')

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	await message.answer("Есть список локаций, все из вас, кроме одного, получают одну из этих локаций, игроки, которые получили локацию должны задавать друг другу вопросы про эту локацию и вычислять того, кто локацию не получил. Человек, который не получил локацию - шпион, ты должен интуитивно отвечать на вопросы, пытайся не спалиться, твоя задача угадать, что это за локация прежде чем тебя вычислят. GLHF")
	await message.answer(locs)
@dp.message_handler(commands=['loc'])
async def command_start(message : types.Message):
	await message.answer(locs)

@dp.message_handler(commands=['newloc'])
async def command_start(message : types.Message):
	await message.answer("Для добавления новой локации отправьте сообщение типа +[название локации]" )

@dp.message_handler(text_contains='+[')
async def about_us(message :types.Message):
	f = filter(str.isalpha, message.text)
	temp = "".join(f)
	locs.append(temp)
	if temp in locs:
		await message.answer("Добавлено!")

@dp.message_handler(commands=['play'])
async def command_start(message : types.Message):
	if len(members) > 1:
		x = random.randint(0, len(members)-1)
		locX = random.randint(0, len(locs)-1)
		await bot.send_message(members[x], "Ты шпион ;)")
		for i in members:
			if i != members[x]:
				await bot.send_message(i, locs[locX])
	else: 
		await message.reply("Слишком мало игроков((")			

@dp.message_handler()
async def about_us(message :types.Message):
	if message.text == '+':
		new = int(message["from"]["id"])
		if new in members:
			await message.reply("Ты уже зарегистрировался")
		if new not in members:
			members.append(new)
			await message.reply("nice")

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)