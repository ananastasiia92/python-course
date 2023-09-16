# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

import random

print(lst := [random.randint(1,20) for i in range(10)])
# count = [1 for i in range(1, len(lst)-1) if lst[i-1]<lst[i] and lst[i]>lst[i+1]]
# print(count)
# print(sum(count))

print(sum(1 for i in range(1, len(lst)-1) if lst[i-1]<lst[i] and lst[i]>lst[i+1]))

# count =0
# for i in range(1, len(lst) - 1):
#     if lst[i-1]<lst[i]>lst[i+1]:
#         count+=1
# print(count)