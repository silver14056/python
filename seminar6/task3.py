"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""
nums = [1, 2, 3, 2, 3, 3, 3, 3]
num_set = set(nums)
res = []

for element in num_set:
    res.append(nums.count(element) // 2)
print(sum(res))

