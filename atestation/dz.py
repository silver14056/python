import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)

# Получаем имя столбца
column_label_lst = [column for column in data]
column_label = column_label_lst[0]

# Получаем список уникальных значений из столбца
column_obj = data[column_label]
print(type(column_obj))
key_lst = list(set(column_obj))

# Добавляем и заполняем новые столбцы
for i in key_lst:
    data.loc[data[column_label] == i, f'{column_label}_{i}'] = '1'
    data.loc[data[column_label] != i, f'{column_label}_{i}'] = '0'

# Удаляем преобразованный столбец
data.drop(column_label, axis=1, inplace=True)
print(data)

