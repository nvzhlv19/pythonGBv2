import re


def show_menu():
    print('1. Распечатать справочник',
    '2. Найти телефон по фамилии',
    '3. Изменить номер телефона',
    '4. Удалить запись',
    '5. Найти абонента по номеру телефона',
    '6. Добавить абонента в справочник',
    '7. Закончить работу',
    'Введите номер действия:', sep='\n')
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if line == '\n':
                pass
            else:
                record = dict(zip(fields, line.rstrip().split(',')))
                phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v+','
            phout.write(f'{s[:-1]}\n')


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while choice != 7:
        if choice == 1:
            print(*phone_book, sep='\n')
        elif choice == 2:
            last_name = input('lastname')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Чтобы изменить номер телефона абонента, введите его фамилию: ')
            print(change_number(phone_book, last_name))
        elif choice == 4:
            last_name = input('Чтобы удалить запись в телефонной книге, введите его фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            print(add_user(phone_book, user_data))
            write_txt('phonebook.txt', phone_book)

        choice = show_menu()


def print_result(phone_book):  # choice 1 печать справочника
    pass


def find_by_lastname(phone_book, last_name):  # choice 2 поиск по фамилии
    for i in phone_book:
        for key in i:
            if i[key].lower() == last_name.lower():
                print(f'Найденные данные: {i["Фамилия"]} {i["Имя"]}{i["Телефон"]}{i["Описание"]}')


def change_number(phone_book, last_name):  # choice 3 изменить номер телефона
    for i in phone_book:
        for key in i:
            if i[key].lower() == last_name.lower():
                print(f'Найденные данные: {i["Фамилия"]}  {i["Имя"]} {i["Телефон"]} {i["Описание"]}')
                flag = input('Номер телефона этого абонента хотите изменить? да или нет?')
                if flag.lower() == 'да':
                    old_number = i['Телефон']
                    new_number = input('Введите новый номер телефона: ')
                    phone_book[phone_book.index(i)]["Телефон"] = new_number
                    with open('phonebook.txt', 'r+', encoding='UTF-8') as f:
                        file = f.read()
                        file = re.sub(str(old_number), str(new_number), file)
                        f.seek(0)
                        f.write(file)


def delete_by_lastname(phone_book, last_name):  # choice 4 удалить запись из телефонного справочника

    for i in phone_book:
        for key in i:
            if i[key].lower() == last_name.lower():
                print(f'Найденные данные: {i["Фамилия"]}  {i["Имя"]} {i["Телефон"]} {i["Описание"]}')
                flag = input('Эту запись удалить? да или нет?')
                if flag.lower() == 'да':
                    with open('phonebook.txt', 'r', encoding='UTF-8') as f:
                        data = f.readlines()
                    with open('phonebook.txt', 'w', encoding='UTF-8') as f:
                        for line in data:
                            if line.strip("\n") != f'{i["Фамилия"]},{i["Имя"]},{i["Телефон"]},{i["Описание"]}':
                                f.write(line)


def find_by_number(phone_book, number):  # choice 5 найти по номеру телефона
    for i in phone_book:
        for key in i:
            if i[key].lower() == number.lower():
                print(f'Найденные данные: {i["Фамилия"]} {i["Имя"]}{i["Телефон"]}{i["Описание"]}')


def add_user(phone_book, user_data):  # choice 6 добавить запись
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.rstrip().split(',')))
    phone_book.append(record)
    return phone_book


work_with_phonebook()
