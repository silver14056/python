def read_t():
    path = 'file.csv'
    data = open(path, 'r')
    print('-------------------')
    for line in data:
        print(line)
    print('-------------------')
    data.close()


def write_t():
    data = open('file.csv', 'a')
    surname_and_telephone = input('Введите фамилию и номер телефона, через пробел(Иванов +791812345678):  ')
    data.writelines(surname_and_telephone)
    data.writelines('\n')
    data.close()


def telephone_book():
    print('Если вам необходимо добавить запись в телефонную книгу, введите W')
    print('Если вам необходимо получить записи из телефонной книги, введите R')
    print('Для выхода введите EXIT')
    key_word = input('Введите ключ: ')
    if key_word.lower() == 'w':
        write_t()
        return True
    elif key_word.lower() == 'r':
        read_t()
        return True
    elif key_word.lower() == 'exit':
        print('--------------------')
        print('Программа завершена')
        print('--------------------')
        return False
    else:
        print('-----------------------')
        print('Вы ввели неверный ключ')
        print('-----------------------')
        return True


flag = True
while flag:
    flag = telephone_book()
