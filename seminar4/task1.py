"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
"""
istr = "a a a b c a a d c d d"
strlist = istr.split()
sdict = {}
for s in strlist:
    if s in sdict:
        sdict[s] += 1
        print(f"{s}_{sdict[s]}", end=' ')
    else:
        sdict[s] = 0
        print(s, end=' ')
"""

input_string = "a a a b c a a d c d d"
words = input_string.split()
counts = {}
result = []
for word in words:
    if word in counts:
        counts[word] += 1
        result.append(f"{word}_{counts[word]}")
    else:
        counts[word] = 0
        result.append(word)
print(" ".join(result))
