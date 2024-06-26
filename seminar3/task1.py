"""Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
"""
# переводим список в множество, теряя повторяющиеся элементы, и выводим длину множества
print(len(set(my_list))) 
"""
"""
# создание массива через ввод с клавиатуры т проверклй на тип
my_list = []
# flag = True
while True: # крутим цикл пока True
try:
my_str = int(input('Введите число, для завершения ввода введите любой символ, кроме числа: '))
except ValueError:
print('Вы ввели строку')
break
else:
my_list.append(my_str)
print(len(set(my_list))) 
"""

# Через for
res = []
for el in my_list:
    if el not in res:
        res.append(el)
print(len(res))


