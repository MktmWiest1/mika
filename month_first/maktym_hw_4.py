# Дан словарь состоящий из основных данных нашего учебного заведения:
GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
# Удалить bag
del GeekTech['bag']
# Изменить адрес на нынешний
GeekTech['address'] = ' ул.Ибраимова 103,БЦ "Victory" 4 этаж ',
# Добавить номер телефона и инстаграмм аккаунт Гиктека
GeekTech['Instagram'] = 'geektech__kg '
GeekTech['phones'] = '0507 05 2018, 0777 05 2018, 0557 05 2018'.split(", ")

# Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в кортеж
GeekTech['courses'].extend(["UX/UI", "IOS", "FullStack", "Английский для программистов"])
GeekTech['courses'] = tuple(GeekTech['courses'])
# Вывести словарь на экран с помощью цикла for с получением всех пар “ключ:
for key, value in GeekTech.items():
    print(f'{key}: {value}')
