# Кортежи - это неизменяемый список.
# В случае защиты каких-либо данных от изменений (намеренных или случайных).
# Кортеж занимает меньше места в памяти и работают быстрее, по сравнению со списками

t = () # создание пустого кортежа print(type(t)) # class <'tuple'> t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue'] t = tuple(colors)
print(t) # ('red', 'green', 'blue') t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
    print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# Можно распаковать кортеж в независимые переменные:

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.

# В списках в качестве ключа используется индекс элемента.
# В словаре для определения элемента используется значение ключа (строка, число).

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓ # right: →
