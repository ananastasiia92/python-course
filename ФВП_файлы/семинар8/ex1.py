phone_book = {}
path = 'fones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for i, contact in enumerate(contacts, 1):
        phone_book[i] = contact.strip().split(';')
    print(phone_book)
    
def save_filed():
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open (path, 'w', encoding= 'UTF-8') as file:
        file.write(data)
    
def show_contacts(pb: dict):
    print()
    for i, contact in pb.items():
        print(f' {i:>3}. {contact [0]:<20} {contact [1]:<20} {contact [2]:<20}')
    print()
    
def new_contact ():
    name =  input ('Введите имя контакта: ')
    phone = input ('Введите телефон: ')
    comment = input ('Введите комментарий: ')
    u_id = max (phone_book. keys ()) + 1
    phone_book[u_id] = [name, phone, comment]
    return name

def find_contact():
    result = {}
    word = input('Введите ключевое слово для поиска: ').lower()
    for i, contact in phone_book.items():
        if word in ''. join(contact):
            result[i] = contact
    return result



def edit_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input ('Введите ID контакта, который хотитет изменить: '))
    c_name, c_phone, c_comment = phone_book[u_id]
    name = input ('Введите новое имя контакта: ')
    phone = input ('Введите новый телефон: ')
    comment = input ('Введите новый комментарий: ')
    phone_book[u_id] = [name if name else c_name, phone if phone else c_phone, 
                        comment if comment else c_comment]
    return name if name else c_name


def del_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input ('Введите ID контакта, который хотите удалить: '))
    name = phone_book.pop
    return name



menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''

while True:
    print(menu)
    choice = int(input('Выберите пункт меню: '))
    if choice == 1:
        open_file()
        print ('\пТелефонная книга успешно загружена!\n')
    elif choice == 2:
        save_filed()
        print ('\nТелефонная книга успешно сохранена!\n')
    elif choice == 3:
        show_contacts(phone_book)
    elif choice == 4:
        name = new_contact()
        print (f' \nКонтакт {name} удачно создан\п')
    elif choice == 5:
        result = find_contact()
        show_contacts(result)
    elif choice == 6:
        name = edit_contact()
        print (f'Контакт {name} успешно изменен!')
    elif choice == 7:
        name = del_contact()
        print (f'Контакт {name} успешно удален!')
    elif choice == 8:
        print('До свидания, всего хорошего!')
        break
    else:
        print('Ошибка ввода! Выберите пункт меню от 1 до 8')