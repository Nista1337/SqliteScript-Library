# -*- coding: utf-8 -*-

from utils.DataBase import DataBase
from utils.Application import Aplication







if __name__ == "__main__":

    db = DataBase('db.db')
    app = Aplication(database=db)
    app.run()
