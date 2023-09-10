# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

string = input('Введите строку: ')
#fhdlshdsns.dkibgdsjsmds.ds.dhstds,/suyy...whrt
dict_count = {} #создаем словарь для подсчета
result_list = []
for i in dict_count: #заносим в словарь с проверкой
    if i in dict_count:
        dict_count[i] = dict_count.get(i)+1
    else:
        dict_count[i]= 1
    if dict_count.get(i) > 1: #забираем значения из словаря с повторениями и заносим в список
        result_list.append(f'{i}_{dict_count.get(i)-1}')
    else:
        result_list.append(i)