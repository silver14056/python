"""
colors = ['red', '222', 'blue']
data = open('file.txt', 'a', encoding='utf-8')  # здесь указывается режим и кодировка.
                                                # если кодировку не указывать, то по умолчанию применится utf-8
data.writelines(colors)     # разделителей не будет
data.close()                # обязательно надо закрыть
"""
"""
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    
print(5)            # как только начнет работать слдующий метод, файл закроется
"""

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
