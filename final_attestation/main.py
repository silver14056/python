from create import create_note


def main():
    print(
        "Это программа заметок. Выберите действие\n"
        "1 - создать заметку\n"
        "2 - вывести заметку\n"
        "3 - редактировать заметку\n"
        "4 - удалить заметку"
    )
    command = int(input("Введите номер операции "))
    while command not in [1, 2, 3, 4]:
        print("Неправильный ввод. Попробуйте еще раз ")
        command = int(input("Введите номер операции:"))

    if command == 1:
        create_note()
    elif command == 2:
        print_note()
    # elif command == 3:
    #     change_note()
    # elif command == 4:
    #     delete_note()


if __name__ == "__main__":
    main()
