stroka = 'пора-ра-рам рам-пам-папам па-ра-па-дам'
"""
ok = 'Парам пам-пам'
not_ok = 'Пам парам'
not_enough = 'Количество фраз должно быть больше одной!'
letters = 'уеыаояиюэ'
"""


def ritm(str1):
    letters = 'уеыаояиюэ'
    list_str = str1.split()
    if len(list_str) < 2:
        print('Количество фраз должно быть больше одной!')
    else:
        list_count = []
        for i in range(len(list_str)):
            count = 0
            for j in list_str[i]:
                if letters.find(j) != -1:
                    count += 1
            list_count.append(count)
        flag = True
        for i in range(len(list_count) - 1):
            if list_count[i] != list_count[i+1]:
                flag = False
        if flag:
            print('Парам пам-пам')
        else:
            print('Пам парам')


ritm(stroka)
