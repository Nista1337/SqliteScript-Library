

class Aplication:

    def __init__(self, database) -> None:
        self.database = database

    def run(self) -> None:

        question = \
            "\nПрограмма для управления книгами Sqlite3\n\n" \
            "Выберите действие:\n\n" \
            "1. Добавление книги\n" \
            "2. Редактировать книгу\n" \
            "3. Найти книгу\n" \
            "4. Удаление книги\n" \
            "5. Вывести список книг\n"
    
        print(question)
        choice = input("Ваш выбор: ")

        if choice == "1":
            self.__add_book()

        elif choice == '2':
            self.__edit_book()

        elif choice == '3':
            self.__find_book()

        elif choice == '4':
            self.__delete_book()

        elif choice == '5':
            self.__show_all_book()

        else:
            print('Неверно! Попробуйте выбрать число из списка!')
            self.run()
    
    def __add_book(self):
        name = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год книги: ')
        
        if not year.isdigit():
            raise TypeError('Год должен быть числом!')

        self.database.insert_table(name=name, author=author, year=year)
        
        print(f'Успешно добавил книгу: {name} | {author} | {year}')
        self.run()

    def __edit_book(self):
        name = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год книги: ')

        if not year.isdigit():
            raise TypeError('Год должен быть числом!')

        book = self.database.find_book(name=name, author=author, year=year)
        if not book:
            print('Данная книга отсутствует в БазеДанных!')
            return

        new_name = input('Введите новое название книги: ')
        new_author = input('Введите новое название книги: ')
        new_year = input('Введите новый год издания: ')



        if not new_year.isdigit():
            raise TypeError('Год должен быть числом!')

        self.database.change_book(name, author, year, new_name, new_author, new_year)
        print('Успешно внес изменения')
        self.run()

    def __find_book(self):
        name = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год книги: ')

        if not year.isdigit():
            raise TypeError('Год должен быть числом!')

        book = self.database.find_book(name=name, author=author, year=year)
        if book:
            print('Данная книга есть в БазеДанных!')
        else:
             print('Данная книга отсутствует в БазеДанных!')

        self.run()

    def __delete_book(self):
        name = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год книги: ')

        if not year.isdigit():
            raise TypeError('Год должен быть числом!')

        book = self.database.find_book(name=name, author=author, year=year)
        if not book:
            print('Данная книга отсутствует в БазеДанных!')
            return

        self.database.delete_book(name=name, author=author, year=year)
        print('Успешно удалил книгу!')
        self.run()
    def __show_all_book(self):
        library = self.database.get_all()
        
        if not library:
            print('У вас нет книг в БазеДанных!')
            return
        
        text = ''
        
        for value, book in enumerate(library, start=1):
            name, author, year = book
            text += f'{value}. Название: {name} | Автор: {author} | Год: {year}\n'
        
        print(text)
        self.run()