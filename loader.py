from aiogram import Bot, Dispatcher, Router
from utils.db_api.db_file import DataBase
from data import config

db = DataBase(config.session_url)



from filters.filters import ChatTypeFilter




bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()




router = Router()
dp.include_router(router=router)
router.message.filter(ChatTypeFilter(['private']))



