# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите пырвый элемент строки: '))
b = int(input('Ведите шаг для строки: '))
c = int(input('Введите кол-во элементов: '))
print(a, b, c)

for i in range(c):
    print(a + i * b, end=' ' )

