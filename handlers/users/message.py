from aiogram import types, F
from loader import db, bot, router
from aiogram.filters import CommandObject
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
import keyboards.inline.keyboard as inline
import data.config as cfg



@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext, command: CommandObject):
    await state.clear()
    boss_id = command.args
    await message.answer_photo(photo=cfg.start_image, caption=f'👋 Приветствую тебя, {message.from_user.first_name}', reply_markup=inline.get_keyboard())
    status = await db.add_user(message.from_user.id, message.from_user.username, boss_id)
    if status:
        try:
            await bot.send_message(boss_id, f'')
        except:
            pass




    
