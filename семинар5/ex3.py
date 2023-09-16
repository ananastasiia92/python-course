# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes
n = 997 # 5/1= 5  5/5=1

def simple_num(n: int)->bool: #берем интовое значение и возвращаем булевое
    # перебирает сдишком много знаечний
    
    # for i in range(2, n):   
    #     if n%i ==0:
    #         return False
    # return True
    
    if n in [1,2]: #отсеиваем первые два числа
        return True
    if n%2 == 0: # отсеиваем все четные числа
        return False
    for i in range(3, n//2 + 1, 2): # сокращаем еще в половину
            if n%i == 0:
                return False
    return True
        
    
        
print(simple_num(n))