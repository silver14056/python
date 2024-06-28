"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
number = "3 4"


def func1(data):
    new_data = ""
    for s in reversed(data):
        new_data += s
    return new_data


print(func1(number))


def func2(data, new_data=""):
    if len(data) == 0:
        return new_data
    return func2(data[:-1], new_data+data[-1])


print(func2(number))
