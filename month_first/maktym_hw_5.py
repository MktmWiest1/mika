contacts = {
    {
        'name': 'Geektech', 'phone': '0507052018'
    },
    {
        'name': 'Служба спасения', 'phone': '911'
    },
    {
        'name': 'Пожарная служба', 'phone': '101'
    },
}

def show_all_contact(lst):
    for i in lst:
        print(*i.values())


def create(lst):
    show_all_contact(contacts)
    for i in lst:
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        n = dict(name=name.title(), phone=phone)
        lst.append(n)
        if i['phone'] == phone:
            print("It's number repeat\n"
                  "Please write wrong!")
        elif i['name'] == name:
            print("It's number repeat\n"
                  "Please write wrong!")
        else:
            show_all_contact(contacts)
            break

def edit(lst):
    show_all_contact(contacts)
    name = input('Введите имя для изминения:')
    for i in lst:
        if i['name'] == name:
            n = input('Введите имя:')
            phone = input('Введите номер:')
            i['name'] = name
            if i['name'] == n:
                print("Номер повторяется!\n"
                      "Пожалуйста напишите неправильно!")
            if i['phone'] == phone:
                print("Номер повторяется!\n"
                      "Пожалуйста напишите неправильно!")
            else:
                i['name'] = n
                i['phone'] = phone
                show_all_contact(contacts)
                break

def delete(lst):
    show_all_contact(contacts)
    name = input('Введите имя для удаления:')
    for i in lst:
        if i['name'] == name:
            lst.remove(i)
            show_all_contact(contacts)
            break

while True:
    command = input("Enter what we'll do: add = 'a', edit = 'e' or delete = 'd'or quite")
    if command == 'a':
        create(contacts)
    elif command == 'e':
        edit(contacts)
    elif command == 'd':
        delete(contacts)
    elif command == 'f':
        print('Программа завершина!')
        break

#
#     contacts.append({'name':name , 'phone': phone})
#
# def edit():
#
#     pass
# def delete():
#
#     pass
# ]
#
# create("Maktym", "953953")
# create("Maktym", "953953")
# for contact in contacts:
#     print(contact)
