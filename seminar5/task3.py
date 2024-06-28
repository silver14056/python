"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
def num_is_prime1(n):
    for i in range  (2, n):
        if n%i==0:
            return "no"
    return "yes"
print(num_is_prime1(6))

def num_is_prime2(n, i=2):
    if i<n:
        if n%i==0:
            return "no"
        return num_is_prime2(n, i+1)
    return "yes"
print(num_is_prime2(6))

