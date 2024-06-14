# if, else, elif(else-if)
"""username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал Вас Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)"""

# while
"""i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит ')
print(i)"""

# Метод флажка
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:  # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2:  # делитель числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
