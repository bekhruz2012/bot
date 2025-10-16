import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = "8367468292:AAHY1zaAUv6VH08dUP1nt4BYMWtdVKiUk74"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Открыть магазин", web_app=types.WebAppInfo(url="https://collaboration-drab.vercel.app/"))],
        [InlineKeyboardButton(text="📦 Мои заказы", callback_data="my_orders")],
        [InlineKeyboardButton(text="💬 Техподдержка", callback_data="support")]
    ])
    await message.answer("Привет! Добро пожаловать в <b>100days</b> 💎", reply_markup=keyboard)

@dp.callback_query(F.data == "my_orders")
async def show_orders(callback: types.CallbackQuery):
    await callback.message.answer("Ваши заказы пока пусты 🛒")

@dp.callback_query(F.data == "support")
async def support(callback: types.CallbackQuery):
    await callback.message.answer("Напишите ваш вопрос, и мы скоро ответим 💬")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
