"""
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной population
 и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
"""

from pandas import read_csv

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

max_households_in_min_population = data[data['population'] == data['population'].min()]['households'].max()
print(max_households_in_min_population)
