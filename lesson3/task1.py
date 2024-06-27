def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sum_numbers(5)


# можно задавать значения по умолчанию
def func(n, str='привет'):
    n += n
    print(n)
    print(str)


func(5)
func(5, 'здрасьте')


# можно передавать неограниченное колличество архументов с помощью звездочки
def sum_str(*args):
    res = ''
    for i in args:
        res += str(i) #  Д\З: чтобы с цифрами канало тоже, добавил привведение к строке
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'i'))
print(sum_str(1, 2, 3, 4, 5))