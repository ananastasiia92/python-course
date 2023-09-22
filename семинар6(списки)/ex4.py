# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. 


def sum_divisors(number): # функция вычисляет сумму всех делителей
    summa = 0
    for i in range(1, number//2 + 1):
        if number%i == 0:
            summa += i
    return summa
# print(sum_divisors(220))
# print(sum_divisors(284))
for num in range(105, 10000):
    frendly_num = sum_divisors(num)
    if num == sum_divisors(frendly_num) and num < frendly_num:
        print(num, frendly_num)
        
def summ_divider(number):
summa = 0
for i in range(1, number // 2 + 1):
if number % i == 0:
summa += i
return summa


friendly_dict = {num: summ_divider(num) for num in range(10000)}

for num in range(10000):
friendly_num = friendly_dict.get(num)
if num == friendly_dict.get(friendly_num) and num < friendly_num:
print(num, friendly_num)

