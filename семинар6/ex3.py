# Дан список чисел. Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента, 
# равные друг другу образуют одну пару, которую необходимо посчитать.


import random

print(lst := [1,2,3,2,3,5,2,2,3]) # 1 2 3 5 

count =[(lst.count(i)//2, i) for i in set(lst)] # кортеж
print(count)

# count =[(lst.count(i)//2) for i in set(lst)]
# for i in set(lst):
#     lst.count(i)//2
#     count+=1
# print(sum(count))


    