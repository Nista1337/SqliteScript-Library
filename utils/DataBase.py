from typing import Optional, Tuple
import sqlite3


class DataBase:
   
    def __init__(self, name: str) -> None:
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("create table if not exists library (name TEXT, author TEXT, year INT)")

    def insert_table(self, name: str, author: str, year: int) -> None:
        
        if not name:
            raise ValueError('Пожалуйста, укажите название книги. Например: Война и мир')
        
        if not author:
            raise ValueError('Пожалуйста, укажите автора книги. Например: А.С Пушкин')
        
        if not year:
            raise ValueError('Пожалуйста, укажите год книги. Например: 1999')

        
        self.cursor.execute('insert or ignore into library (name, author, year) VALUES (?, ?, ?)', (name, author, year))
        self.conn.commit()
    
    def get_all(self) -> list:
        library = self.cursor.execute('select * from library')
        return library.fetchall()
    
    def find_book(self, name: str, author: str, year: int) -> Optional[Tuple]:
        
        if not name:
            raise ValueError('Пожалуйста, укажите название книги. Например: Война и мир')
        
        if not author:
            raise ValueError('Пожалуйста, укажите автора книги. Например: А.С Пушкин')
        
        if not year:
            raise ValueError('Пожалуйста, укажите год книги. Например: 1999')

        book = self.cursor.execute('select * from library where name = ? and author = ? and year = ?', (name, author, year))
        return book.fetchone()

    def change_book(self, name: str, author: str, year: int, new_name: str, new_author: str, new_year: int) -> None:
        
        if not name:
            raise ValueError('Пожалуйста, укажите название книги. Например: Война и мир')
        
        if not author:
            raise ValueError('Пожалуйста, укажите автора книги. Например: А.С Пушкин')
        
        if not year:
            raise ValueError('Пожалуйста, укажите год книги. Например: 1999')

        if not new_name:
            raise ValueError('Пожалуйста, укажите новое название книги. Например: Война и мир')
        
        if not new_author:
            raise ValueError('Пожалуйста, укажите нового автора книги. Например: А.С Пушкин')
        
        if not new_year:
            raise ValueError('Пожалуйста, укажите новый год книги. Например: 1999')

        self.cursor.execute('update library set name = ?, author = ?, year = ? WHERE name = ? and author = ? and year = ?', (new_name, new_author, new_year, name, author, year))
        self.conn.commit()

    def delete_book(self, name: str, author: str, year: int) -> None:

        if not name:
            raise ValueError('Пожалуйста, укажите название книги. Например: Война и мир')
        
        if not author:
            raise ValueError('Пожалуйста, укажите автора книги. Например: А.С Пушкин')
        
        if not year:
            raise ValueError('Пожалуйста, укажите год книги. Например: 1999')

        self.cursor.execute('delete from library where name = ? and author = ? and year = ?', (name, author, year))
        self.conn.commit()
        