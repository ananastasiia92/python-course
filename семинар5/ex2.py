# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

import random

MIN_1= 1
MAX_1= 10
print(journal := [random.randint(MIN_1, MAX_1) for i in range(6)])
# := моржовый оператор, одновременно выводит и присваивает

def change_mark(lst: list):
    maximum = max(lst)
    minimum = min(lst)
    for i in range(len(lst)):
        if lst[i] == maximum:
            lst[i] = minimum

change_mark(journal)
print(journal)
            
    