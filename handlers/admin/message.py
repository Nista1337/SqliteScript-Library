from aiogram import types, F
from loader import db, bot, dp, router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from filters.filters import IsAdmin





@dp.message(IsAdmin(), Command('admin'))
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("admin panel!")
