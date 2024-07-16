"""
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей
от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""

from pandas import read_csv

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

avg = data[(data['population'] > 0) & (data['population'] < 500)]['median_house_value'].mean()
print(avg)
