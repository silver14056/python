import csv


def read_note():
    with open("notes.csv", "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=";", skipinitialspace=True)
        print()
        for row in data:
            print(
                f"Заметка №{row[0]}\nЗаголовок: {row[1]}\nЗаметка: {row[2]}\nДата: {row[3]}\n"
            )
