import json from aiogram import Bot, Dispatcher, types from aiogram.utils import executor
ТOKEN = "8799292585:AAEYvtMqetJDL3GUP06DwScLOvyrGOoudkM" ADMIN_ID = 5355079875
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
try:
with open("users.json", "r") as f:
data = json.load(f)
except:
data =
def save():
with open("users.json", "w") as f:
json. dump(data, f)
@dp.message_handler(commands=['start']) async def start(messaae: types.Message):
user_id = str(message.from_user.id)
if user_id not in data:
     data[user_ID]=0
     save()

await message.answer (f"Ты зарегестрирован\nТвой ID:  {user_id}")
@dp.message_handler(commands= ['balance']) async def balance(message: types.Message): user_id = str(message.from_user.id) bal = data.get(user_id, 0)
await message.answer(f"Баланс: {bal} ⭐")
@dp.message_handler(commands=['add']) async def add_balance(message: types.Message): if message.from_user.id != ADMIN_ID: return
try:
    _, user_id, amount =message.text.split()
    user_id = str(user_id)
    amount = int(amount)

            data[user_id] = 0

    data[user_id] += amount
    save()
await message.answer(f"Начислено {amount}⭐ пользователю {user_id}")

except:
    await message.answer("Формат: /add user_id сумма")
@dp.message_handler(commands=['withdraw'])
async def withdraw(message: types.Message):
await message.answer("Напиши сумму и отправь скрин админу @red0relayer")

if name == "main":
executor.start_polling(dp)
