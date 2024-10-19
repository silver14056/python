import csv
from check_id import check_id


def read_note():
    print("--------------------------------------------------")
    print(
        "Вывести все заметки - 1\nвывод заметки по номеру - 2"
    )
    print("--------------------------------------------------")
    command = int(input("Введите номер операции:"))
    while command not in [1, 2]:
        print("--------------------------------------------------")
        print("Неправильный ввод. Попробуйте еще раз!")
        command = int(input("Введите номер операции:"))

    if command == 1:
        with open("notes.csv", "r", encoding="utf-8") as f:
            data = csv.reader(f, delimiter=";", skipinitialspace=True)
            print()
            for row in data:
                print(
                    f"Заметка №{row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}\n"
                )
    elif command == 2:
        print("--------------------------------------------------")
        num_id = int(input("Введите номер заметки для просмотра:"))
        if check_id(num_id):
            with open("notes.csv", "r", encoding="utf-8") as f:
                data = csv.reader(f, delimiter=";", skipinitialspace=True)
                for row in data:
                    if int(row[0]) == num_id:
                        print(
                            f"\nЗаметка №{row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}\n"
                        )
        else:
            print("--------------------------------------------------")
            print("Заметки с таким номером нет!")
