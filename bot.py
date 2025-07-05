import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привіт, друже! Я — АрхеоКОП, твій помічник у світі артефактів! 🔍\n"
        "Надсилай фото чи опис знахідки — і я допоможу її визначити!\n"
        "Спробуй команди: /допомога /визначити /дайджест /вікторина"
    )

@dp.message(Command("допомога"))
async def help_command(message: Message):
    await message.answer(
        "📌 Доступні команди:\n"
        "/визначити — надішли опис або фото артефакта\n"
        "/новини — останні археологічні новини\n"
        "/дайджест — щоденний огляд подій\n"
        "/вікторина — загадка або квест\n"
        "/анекдот — трохи історичного гумору"
    )

@dp.message(Command("анекдот"))
async def joke(message: Message):
    await message.answer("Язичники стоять перед ідолом і моляться. А ідол каже: «Перейдімо на цифру!» 😄")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())