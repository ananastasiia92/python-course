# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
coins = int(input('Введите кол-во монет: '))

count1 = 0
count2 = 0
min_count = 0
for i in range(coins):
    revers = random.randint(0, 1)
    print(revers, end= " ")
    
    if revers == 0:
        count1 += 1
    if revers == 1:
        count2 += 1
    if count1 > count2:
        min_count = count2
    else:
        min_count = count1

    
        
print(f'\n Минимальное количество монет которые нужно перевернуть {min_count}')
        
        

        