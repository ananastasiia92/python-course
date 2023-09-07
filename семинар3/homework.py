

import random

list = [random.randint(0, 30) for i in range (8)]
print (list)

k = int(input('Введите число: '))
count = 0

for i in range((len(list))):
    
    if list[i]==k:
        count+=1
        print(count)
        break
    else:
        n = abs(k-list[0])
        for i in range(len(list)-1):
            if abs(k-list[0]) > abs(list[i]-k):
                n = abs(list[i]-k)
                next = list[i]

print(f'\nЧисло ближайшее по значению: {next}')




