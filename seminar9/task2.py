"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых двух столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
"""

from pandas import read_csv

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

# 1. Проверить есть ли в файле пустые значения

print(data.isnull().sum())

# 2. Показать median_house_value где median_income < 2

print(data[data['median_income'] < 2]['median_house_value'])

# 3. Показать данные в первых двух столбцах

print(data[['longitude', 'latitude']])
print(data.iloc[:, :2])

# 4. Выбрать данные где housing_median < 20 и median_house_value > 70000

print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)])
