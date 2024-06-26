n = int(input("Введите число (0 для выхода): "))
max_number = -1
while n != 0:
    n = int(input("Введите число (0 для выхода): "))
    if max_number < n:
        max_number = n
print(max_number)