"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

list1 = [1, 3, 3, 3, 4]
# цикл
min_grade = min(list1)
max_grade = max(list1)
list2 = []
for grade in list1:
    if grade == max_grade:
        list2.append(min_grade)
    else:
        list2.append(grade)
print(list2)

# comprehension
print([min_grade if grade == max_grade else grade for grade in list1])


# рекурсия
def func(list1, list2=[], min_grade=min(list1), max_grade=max(list1)):
    if len(list1) == 0:
        return list2
    if list1[0] == max_grade:
        list2.append(min_grade)
    else:
        list2.append(list1[0])
    return func(list1[1:], list2)


print(func(list1))
