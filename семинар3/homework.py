

import random

list = [random.randint(0, 30) for i in range (8)]
print (list)

k = int(input('Введите число: '))
# count = 0

# for i in range((len(list))):
    
#     if list[i]==k:
#         count+=1
#         print(count)
#         break
#     else:
#         n = abs(k-list[0])
#         next = list[0]                  #4-23 = -19
#         for i in range(len(list)-1):    #-19 > 6-4 =2
#             if n > abs(list[i]-k):      
#                 n = abs(list[i]-k)
#                 next = list[i]

# print(f'\nЧисло ближайшее по значению: {next}')

if k in list:
    result = f'Число {k} встречается в списке {list. count (k)} раз'
else:
    min_dist = abs (list [0] - k)
    nearest = list [0]
for num in list:
    if (dist := abs (num - k)) < min_dist:
        nearest = num
        min_dist = dist
    result = f'Ближайшее число к {k} будет {nearest}'

print(result)




