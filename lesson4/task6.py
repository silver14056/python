# zip
users1 = ['user1', 'user2', 'user3', 'user4', 'user5']
ids1 = [4, 5, 9, 14, 7]
data1 = list(zip(users1, ids1))
print(data1)  # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# если не равное количество элементов в списках то будет минимально возможное колличество комплектов
users2 = ['user1', 'user2', 'user3', 'user4', 'user5']
ids2 = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data2 = list(zip(users2, ids2, salary))
print(data2)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
