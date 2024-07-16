"""
Задача №1
1. Прочесть с помощью Pandas файл
2. Получить количество строк и столбцов
3. Определить, какой тип данных имеют столбцы
"""

from pandas import read_csv

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

print(type(data))
print('--------------------')
print(data.shape)
print('--------------------')
print(data.dtypes)
print('--------------------')
print(data.info())
print('--------------------')
print(data.describe())
print('--------------------')
