import asyncio
from loader import dp, db, bot
from utils.set_bot_commands import set_default_commands
import logging
import handlers
import data
import filters


async def on_startup():
    await db.check_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await set_default_commands(bot)
    await dp.start_polling(bot)





if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(on_startup())
    except Exception as err:
        logging.exception(err)

