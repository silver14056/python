from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 ВариантЖ \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Ввелите правильное число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = -1
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                j += 1
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def change_data():
    var = int(input("В какую телефонную книгу будем вносить изменения: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите правильное число: '))
    key = int(input("Введите номер записи которую нужно изменить: "))
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = -1
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    j += 1
                    data_first_list.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first_list[key - 1] = f"{name}\n{surname}\n{phone}\n{address}\n\n"
            print((''.join(data_first_list)))
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_first_list))
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second[key - 1] = f"{name};{surname};{phone};{address}\n"
            print(*data_second)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_second))


def delete_data():
    var = int(input("В какую телефонную книгу будем вносить изменения: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите правильное число: '))
    key = int(input("Введите номер записи которую нужно удалить: "))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = -1
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    j += 1
                    data_first_list.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first_list.pop(key - 1)
            print((''.join(data_first_list)))
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_first_list))
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second.pop(key - 1)
            print(*data_second)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_second))
