# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))

i = 0
j = 0
while j < n:
    j = 2**i
    print(j, end= ' ')
    i = i+1

    