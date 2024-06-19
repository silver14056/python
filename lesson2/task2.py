
"""list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
list_1.append(85)
print(list_1)
"""
"""
list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)
    """
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1)       # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1)       # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1)       # [12, 7]
"""
# pop - удвляет и возвращает последний елемент, а если передать в pop индекс элемента, то удалит именно его
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1)       # [7, -1, 21б 0]
"""

# добавление элемента на нужную позицию
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1)
"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                    # 1
print(list_1[1])                    # 2
print(list_1[len(list_1) - 1])      # 10
print(list_1[-5])                   # 6
print(list_1[:])                    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                   # [1, 2]
print(list_1[len(list_1)-2:])       # [9, 10]
print(list_1[2:9])                  # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                # []
print(list_1[0:len(list_1):6])      # [1, 7]
print(list_1[::6])                  # [1, 7]


