# кортеж неизменяемый список тип tuple
"""
t = ()
print(type(t))
print()

t = (1)
print(type(t))  # <class 'int'>
t = (1,)        # чтобы получился кортеж, нужна запятая после последнего элемента
print(type(t))  # <class 'tuple'>

t = (1, 3, 5,)
print(type(t))  # <class 'tuple'>

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v       # распаковка кортежа
print(a, b, c)
"""

t = (1, 2, 3, 5,)
print(t[1])
print('***')

for i in t:
    print(i)
print('***')

for i in range(len(t)):
    print(t[i])
print('***')