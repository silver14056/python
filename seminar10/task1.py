"""
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""

from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show

df = read_csv('california_housing_test.csv')

# 1. Изобразите отношение households к population с помощью точечного графика
"""
scatter_plot = scatterplot(data=df, x='households', y='population')
scatter_plot.set_title('Название графика')
scatter_plot.set_xlabel('Название оси X')
scatter_plot.set_ylabel('Название оси Y')
show()
"""
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
"""
relplot(data=df, x='longitude', y='median_house_value', kind='line')
show()
"""
# 3. Представить гистограмму по housing_median_age
"""
histplot(data=df, x='housing_median_age')
show()
"""
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

histplot(data=df, x='median_house_value', hue='housing_median_age')
show()
