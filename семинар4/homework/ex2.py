# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.i ягод.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import random

list = [random.randint(0, 100) for i in range (10)]
print (list)
for i in range(2):
    list.append(list[i])
print(list)
sum1 =[]

for i in range(len(list)-2):
   sum1.append(sum(list[i : i+3]))
   max1 = sum1[0]
   for j in sum1:       
       if j > max1:
           max1 = j
           j+=1

print(sum1)
print(f'\n Максимальное число ягод: {max1}')

    




