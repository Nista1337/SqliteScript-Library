from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def get_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="🗃 Открыть кейс", callback_data="open_box"),
        ],
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
         [
            InlineKeyboardButton(text="📥 Вывести средства", callback_data="output")
         ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard