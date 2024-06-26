
# заполнение списка значениями с помощью цикла for
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)           # [1, 2, 3,....100]

# то же самое но используется list comprehension (вроде как запись в одну строку)
list_2 = [i for i in range(1, 101)]
print(list_2)

# comprehension с условием
list_3 = [i for i in range(1, 101) if i%2==0] # только чётные
print(list_3)
list_4 = [(i, i) for i in range(1, 101) if i%2==0] # чётные парами в кортежах
print(list_4)
list_5 = [i*2 for i in range(10) if i%2==0] # можно использовать математические действия
print(list_5)

