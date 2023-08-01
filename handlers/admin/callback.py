from aiogram import types, F
from loader import db, bot, dp, router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from filters.filters import IsAdmin


@dp.callback_query(IsAdmin(), F.data == (''))
async def callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('1111')

