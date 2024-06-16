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
"""n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:  # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2:  # делитель числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1"""

# for и range

"""line = ""
for i in range(3):
    line = ""
    for j in range(5):
        line += "*"
    print(line)"""

#Строки
"""text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'ЕЩЁ'))"""

#срез строк
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(text[0])                              # с
print(text[1])                              # ъ
print(text[len(text) - 1])                  # к
print(text[-5])                             # б
print(text[:])                              # СъЕШЬ ещё этих МяГкИх французских булок
print(text[:2])                             # съ
print(text[len(text) - 2:])                 # ок
print(text[2:9])                            # ЕШЬ ещё
print(text[6:-18])                          # ещё этих МяГкИх
print(text[0:len(text):6])                  # Сеикакл
print(text[::6])                            # Сеикакл
text = text[2:9] + text[-5] + text[:2]      # ...
print(text)                                 # ЕШЬ ещёбСъ
