"""
colors = {'red', 'green', 'blue'}
print(colors)           # {'red', 'green', 'blue'}
colors.add('red')
print(colors)           # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)           # {'red', 'green', 'blue', 'gray'}
colors.remove('red')
print(colors)           # {'green', 'blue', 'gray'}
# colors.remove('red')    # KeyError: 'red'
colors.discard('red')   # ok
print(colors)           # {'green', 'blue', 'gray'}
colors.clear()          # { }
print(colors)           # set()
"""

# Операции с множествами
"""
a = {1, 2, 3, 5, 8}
print(a)                                        # {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
print(b)                                        # {2, 5, 21, 8, 13}
c = a.copy()
print(c)                                        # {1, 2, 3, 5, 8}
u = a.union(b)
print(u)                                        # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)
print(i)                                        # {8, 2, 5}
dl = a.difference(b)
print(dl)                                       # {1, 3}
dr = b.difference(a)
print(dr)                                       # {13, 21}
q = a.union(b).difference(a.intersection(b))
print(q)                                        # {1, 21, 3, 13}
"""

a = {1, 8, 6}

b = frozenset(a) # создаём множество b(копию a), которое нельзя изменять


