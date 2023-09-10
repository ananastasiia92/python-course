# Дан список чисел. Определите, сколько в нем встречается различных чисел.

#list = [3, 3, 6, 4, 6, 7, 5, 9, 2, 2, 8, 3, 0, 3, 7, 3, 4, 0, 1, 1, 2]
#print(list)
#list = set(list)
#print(len(list))

# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.



#list2 = [3, 3, 6, 4, 6, 7, 5, 9, 2, 2, 8]

#k = int(input("Введите колво элементов: "))

#tmp = (list2[len(list2)-k:])
#print(tmp)
#list = tmp + list2
#print(list)
#or
import random
lst = []
#for i in range (10):
#    lst.append (random. randint (0, 100))
#or
lst = [random.randint(0, 100) for i in range (10)]
print (lst)
shift = int(input("Введите сдвиг: "))

# print (lst[:-shift])
# print (lst[-shift:])
# lst = lst[-shift:] + lst[:-shift]
# print (lst)
#or
# for i in range (shift):
#     lst.insert(0, lst.pop (-1)) 
# print (lst)

#or

for i in range (len (lst)):
    print (lst[(i - shift)%len(lst)], end=', ')
