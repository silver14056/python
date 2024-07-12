from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 5:
                raise NameError("Слишком короткая фамилия")
            phone = input("Введите номер телефона: ")
            if len(phone) < 11:
                raise NameError("Слишком короткий номер телефона")
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, last_name, phone]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standart_write(file_name, res)


def row_search(file_name):
    last_name = input("Введите фамилию: ")
    res = read_file(file_name)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"


def delete_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    res.pop(row_number - 1)
    standart_write(file_name, res)


def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    data = get_data()
    res[row_number - 1]['Имя'] = data[0]
    res[row_number - 1]['Фамилия'] = data[1]
    res[row_number - 1]['Телефон'] = data[2]
    standart_write(file_name, res)


def copy_row_to_file(file_name, another_file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    another_res = read_file(another_file_name)
    another_res.clear()
    another_res.append(res[row_number - 1])
    standart_write(another_file_name, another_res)


filename = 'phone.csv'
another_filename = 'another_phone.csv'


def main():
    while True:
        command = input(
            "Q-Выход, W-Записать, R-Прочитать, F-Найти, D-Удалить, C-Изменить, M-Копировать в файл\n"
            "Введите команду: ")
        if command.lower() == "q":
            break
        elif command.lower() == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command.lower() == "r":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            for row in read_file(filename):
                print(row, end='\n')
        elif command.lower() == 'f':
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command.lower() == 'd':
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(filename)
        elif command.lower() == 'c':
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            change_row(filename)
        elif command.lower() == 'm':
            if not exists(filename):
                print("Исходный файл не существует. Создайте его.")
                continue
            if not exists(another_filename):
                create_file(another_filename)
                continue
            copy_row_to_file(filename, another_filename)


main()
