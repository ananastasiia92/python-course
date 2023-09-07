# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

import random

list = [random.randint(0, 100) for i in range (10)]
print (list)
count = 0
for i in range(len(list) - 1):
    
    if list[i]<list[i+1]:
        count+=1
print(count)

print(sum([1 for i in range(len(list)-1) if list[i]<list[i+1]]))