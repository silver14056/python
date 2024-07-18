"""
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

"""

from pandas import read_csv
from seaborn import scatterplot, relplot, histplot, load_dataset, PairGrid, heatmap, displot
from matplotlib.pyplot import show, hist, scatter, xlabel, ylabel

penguins = load_dataset('penguins')

# Использовать 2-3 точечных графика
"""
scatterplot(data=penguins, x='sex', y='body_mass_g')
show()
"""
# Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
"""
scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', size='bill_length_mm', hue='bill_length_mm',
            sizes=(10, 300))
scatterplot(data=penguins, x='body_mass_g', y='bill_length_mm', hue='island', style='species')
show()
"""
# Использовать PairGrid с типом графика на ваш выбор
"""
data_columns = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
graph = PairGrid(penguins[data_columns], hue='body_mass_g', palette='deep')
graph = graph.map_diag(hist)  # графики по диагонали
graph = graph.map_offdiag(scatter)  # типы остальных графиков
show()
"""
# Изобразить Heatmap
"""
data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
heatmap(data)
xlabel('Остров', size=14)
ylabel('Вид пингвина', size=14)
show()
"""
# Использовать 2-3 гистограммы

penguins['bill_depth_mm'].hist(bins=10)
displot(data=penguins, x='body_mass_g', kind='hist')
show()
