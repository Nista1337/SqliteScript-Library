from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select, update


Base = declarative_base()



class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String)
    balance = Column(Integer, default=0)
    boss_id = Column(BigInteger)
    lvl = Column(Integer, default=1)


class DataBase:
    def __init__(self, database):
        self.database = database

    async def check_start(self):
        engine = create_async_engine(url=self.database, echo=False)
        session = async_sessionmaker(engine, expire_on_commit=False)
        
        
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async with session() as cursor:
            self.cursor = cursor

    
    async def add_user(self, user_id: int, username: str, boss_id: int = 0) -> None:
        status = True
        sql = select(Users).where(Users.user_id == user_id)
        t = (await self.cursor.execute(sql)).fetchone()
        if t:
            sql = update(Users).where(Users.user_id == user_id).values(username = username)
            await self.cursor.execute(sql)
            await self.cursor.commit()
            status = False
        else:
            if boss_id:
                sql = select(Users).where(Users.user_id == boss_id)
                boss_id_info = (await self.cursor.execute(sql)).fetchone()
                if not boss_id_info:
                    boss_id = 0
                    status = False
            await self.cursor.merge(Users(user_id=user_id, username=username, boss_id = boss_id))
            await self.cursor.commit()

        return status

    async def change_balance(self, user_id, amount):
        sql = update(Users).where(Users.user_id == user_id).values(balance = Users.balance + amount)
        await self.cursor.execute(sql)
        await self.cursor.commit()
# update(Table).where(Table.id=1).values(Table.balance=Table.balance + 1)



    # async def get_ban(self, user_id: int) -> bool:
    #     sql = select(Users).where((Users.user_id == user_id) & (Users.banned == 1))
    #     f = await self.cursor.execute(sql)
    #     return f.fetchone()