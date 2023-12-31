list_1 = [] # Создание пустого списка
list_2 = list() #Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]

print(list_1[0]) #номер элемента

print(len(list_1)) #кол-во элементов


# заполнение во время работы программы

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
    n = int(input()) # пользователь вводит целое число
    list_1.append(n) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 2
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
    print(list_1) # [12, 7, -1, 21, 0]
    
# взаимодействие цикла for со списком

list_1 = [12, 7, -1, 21, 0]
for i in list_1:
    print(i) # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): i = 12
# 2-я итерация цикла(повторение 2): i = 7
# 3-я итерация цикла(повторение 3): i = -1
# 4-я итерация цикла(повторение 4): i = 21
# 5-я итерация цикла(повторение 5): i = 0


# нумерация списка

list_1 = [12, 7, -1, 21, 0]
for i in range(len(list_1)):
    print(list_1[i]) # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): list_1[0] = 12
# 2-я итерация цикла(повторение 2): list_1[1] = 7
# 3-я итерация цикла(повторение 3): list_1[2] = -1
# 4-я итерация цикла(повторение 4): list_1[3] = 21
# 5-я итерация цикла(повторение 5): list_1[4] = 0

# Удаление последнего элемента списка

list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0 
print(list_1) # [12, 7, -1, 21] 
print(list_1.pop()) # 21 
print(list_1) # [12, 7, -1] 
print(list_1.pop()) # -1 
print(list_1) # [12, 7]

# Удаление конкретного элемента списка

list_1 = [12, 7, -1, 21, 0] 
print(list_1.pop(0)) # 12 
print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.

list_1 = [12, 7, -1, 21, 0] 
print(list_1.insert(2, 11)) 
print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк?
# Также существует срез списка, давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) #10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3,4,5,6,7,8,9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) #[1,7]
print(list_1[::6]) # [1, 7]







 