from logger import input_data, print_data, change_data, delete_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains!\n1 - Запись\n2 - Вывод\n"
          "3 - Изменение\n4 - Удаление")
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод")
        command = int(input('Ввелите число: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()
