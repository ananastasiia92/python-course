# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!

import random

min1 = 1000
max1 = 30000

watermelon = int(input('Введите кол-во арбузов: '))

min_weigh = max1
max_weigh = min1
    
for i in range(watermelon):
    weigh = random.randint(min1, max1)
    print(weigh, end= " ")

    if min_weigh > weigh:
        min_weigh = weigh
    if max_weigh < weigh:
        max_weigh = weigh
print(f'\nАрбуз для себя: {min_weigh} \nАрбуз для тещи: {max_weigh}')
        