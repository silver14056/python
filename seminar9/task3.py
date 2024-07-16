"""
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value
"""

from pandas import read_csv

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

# 1. Определить какое максимальное и минимальное значение median_house_value

print(f'Минимальное - {data["median_house_value"].min()}, Максиамльное - {data["median_house_value"].max()}')
print('--------------------')

# 2. Показать максимальное median_house_value, где median_income = 3.1250

print(data[data['median_income'] == 3.1250]['median_house_value'].max())
print('--------------------')

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())
print('--------------------')
