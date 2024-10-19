import csv
from check_id import check_id


def delete_note():
    list_row = []
    print("--------------------------------------------------")
    del_id = int(input("Введите номер записи для удаления:"))
    if check_id(del_id):
        with open("notes.csv", "r", encoding="utf-8") as d:
            data = csv.reader(d, delimiter=";", skipinitialspace=True)
            for rows in data:
                if int(rows[0]) != del_id:
                    list_row.append(";".join(rows))
        with open("notes.csv", "w+", encoding="utf-8") as f:
            for item in list_row:
                f.writelines(f"{item}\n")
        print("--------------------------------------------------")
        print("Удалено")
    else:
        print("--------------------------------------------------")
        print("Такой записи нет")
