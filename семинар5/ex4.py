# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

def insert_nums(n):
    if n == 0:
        return ''
    data = input('Ввод: ')
    return insert_nums(n-1) + data
print(insert_nums(5))


        