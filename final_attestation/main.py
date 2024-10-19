from create import create_note
from read import read_note
from change import change_note
from delete import delete_note


def main():
    flag = True
    while flag:
        print("--------------------------------------------------")
        print(
            "Это программа заметок. Выберите действие:\n"
            "1 - Создать заметку\n"
            "2 - Вывести заметки\n"
            "3 - Редактировать заметку\n"
            "4 - Удалить заметку\n"
            "5 - Выйти из программы"
        )
        print("--------------------------------------------------")
        command = int(input("Введите номер операции:"))
        while command not in [1, 2, 3, 4, 5]:
            print("--------------------------------------------------")
            print("Неправильный ввод. Попробуйте еще раз!")
            command = int(input("Введите номер операции:"))

        if command == 1:
            create_note()
        elif command == 2:
            read_note()
        elif command == 3:
            change_note()
        elif command == 4:
            delete_note()
        elif command == 5:
            flag = False


if __name__ == "__main__":
    main()
