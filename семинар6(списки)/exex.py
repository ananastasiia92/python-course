# функции высшего порядка
# -map

# lst = list ('123fkfjdfhd4567sdsgdfsjnd89amsnajbd0')
lst = list ('1234567890')
print (lst)
# for i in range (len (lst)):
#     lst[i] = int(lst[i])
new_lst = list('ABRTYUIBPR')
# new_lst = list(map(int, lst))
print (new_lst)

# -filter

# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False

# lambda x: x%2 ==0 #простая однострочная анонимная функция с одним IF

# new_lst = []  
# for i in range(len(lst)):
#     if is_even == (lst[i]):
#         new_lst.append(lst[i])
# print(new_lst)

# lst = list(filter(is_even,lst))
# lst = list(filter(lambda x: x%2 == 0,lst))
# lst = list(filter(lambda x: x.isdigit(),lst))
# lst = list(map(int, filter(lambda x: x.isdigit(),lst)))
# lst = list(filter(lambda x: x.isalpha(),lst)) #istitle - проверка только на заглавные буквы

# my_lst =[]
# for i in range(len(lst)):
#     my_lst.append((lst[i],new_lst[i]))
punct = list('@#$%^&&%#@#$^(())')
from itertools import zip_longest
my_lst = list(zip_longest(lst, new_lst, punct, fillvalue = 0))

print(my_lst)