"""
d = {}      # пустой словарь
d = dict()  # пустой словарь

d['q'] = 'qwerty'
print(d)

d['w'] = 'qwerty'
print(d)

print(d['w'])
"""

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
"""
print(dictionary)           # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left'])   # ←
print(dictionary['up'])   # ↑
dictionary['left'] = '⇐'
print(dictionary['left'])   # ⇐
# print(dictionary['type'])   # KeyError: 'type'
del dictionary['left']      # удаление элемента
for item in dictionary:
    print(('{}: {}'.format(item, dictionary[item])))
# up: ↑
# down: ↓
# right: →
dictionary[2343] = 'qwefhe90h903'
print(dictionary)
"""

print(dictionary.items())       # вывод кортежем
for (k,v) in dictionary.items():
    print(k,v)


