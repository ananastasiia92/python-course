# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

import random
size_1 = int(input('Введите длину списка 1: '))
size_2 = int(input('Введите длину списка 2: '))

print(list_1 := [random.randint(1, 10) for i in range (size_1)])

print(list_2 := [random.randint(1, 10) for i in range (size_2)])

print(res := [i for i in list_2 if i not in list_1])

# for i in list_2:
#     if i not in list_1:
#         res.append(i)
# print(res)
        
        