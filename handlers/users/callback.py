from aiogram import types, F
from loader import dp, db, bot, router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext


@router.callback_query(F.data == ('num_finish'))
async def callback(call: types.CallbackQuery, state: FSMContext):
    ...

