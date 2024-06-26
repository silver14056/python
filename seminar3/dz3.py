"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать,
что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:
k = 'ноутбук'
# 12
"""

k = 'ноутбук'

# Введите ваше решение ниже
"""
chars1Point = 'AEIOULNSTRАВЕИНОРСТ'
chars2Point = 'DGДКЛМПУ'
chars3Point = 'BCMPБГЁЬЯ'
chars4Point = 'FHVWYЙЫ'
chars5Point = 'KЖЗХЦЧ'
chars8Point = 'JXШЭЮ'
chars10Point = 'QZФЩЪ'

wordK = k.upper()
points = 0

for i in range(len(k)):
    if chars1Point.find(wordK[i]) != -1:
        points += 1
    if chars2Point.find(wordK[i]) != -1:
        points += 2
    if chars3Point.find(wordK[i]) != -1:
        points += 3
    if chars4Point.find(wordK[i]) != -1:
        points += 4
    if chars5Point.find(wordK[i]) != -1:
        points += 5
    if chars8Point.find(wordK[i]) != -1:
        points += 8
    if chars10Point.find(wordK[i]) != -1:
        points += 10
print(points)
"""

# ЭТАЛОННОЕ РЕШЕНИЕ
letters = 'AEIOULNSTRАВЕИНОРСТDGДКЛМПУBCMPБГЁЬЯFHVWYЙЫKЖЗХЦЧJXШЭЮQZФЩЪ'
points = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in letters:
        for j in points:
            if i in points[j]:
                count = count + j
print(count)