# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
import random

print(list_1 := [15, 37, 21, 43])

char2 = lambda x : x%10 ==0
char3 = lambda x : x %2 ==0

def same_by(characteristic, objects):
    result = list (map (characteristic, objects))
    print(set(result))
    if len(set (result)) == 1 and set(result) == True or False:
        return True
    return False
    # print(result)
    # return all(result) #any вернет тру если есть хотя бы один тру

print(same_by(char2, list_1))
print(same_by(char3, list_1))
