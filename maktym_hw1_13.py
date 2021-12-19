# Задание :
# 1. Создать суперкласс Animal и его классы (пример : Млекопитающие , Пресмыкающиеся) они
# должны быть связаны через наследование
# 2. Класс Animal имеет общие параметры животных
# 3. Класс Млекопитающих и других имеют свои особенные атрибуты и методы
# 4. Создать объекты животных и его классов
# Дополнительные указания к дз:
# 1. Создать класс объекта Zoo_show
# 2. До выбора билета , должно высвечиваться подробная информация о видах шоу
# 3. У этого класса будет метод для выбора билета , при выборе определенного шоу должно
# выходить их цена и как проходит само шо


class Animal:
    def __init__(self, name, color, weight, height):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('Weight should be int')
        if isinstance(height, int):
            self.height = height
        else:
            raise ValueError('Height should be int')

    def __str__(self):
        return f'name:{self.name}\n' \
               f'color: {self.color}\n' \
               f'weight: {self.weight}kg\n' \
               f'height: {self.height}sm'


animal_1 = Animal(name='fox', color='ginger', weight=10, height=90)
print(animal_1)


class Mammal(Animal):
    def __init__(self, name, color, weight, height, milk_feeding):
        super().__init__(name, color, weight, height)
        if isinstance(milk_feeding, str):
            self.milk_feeding = milk_feeding
        else:
            raise ValueError('Milk_feeding should be str')

    def __str__(self):
        return super(Mammal, self).__str__() + f'\n milk_feeding:{self.milk_feeding}  '


mammal_1 = Mammal(name='fox', color='ginger', weight=10, height=90, milk_feeding='no')
print(mammal_1)


class Adjoining(Animal):
    def __init__(self, name, color, weight, height, notmilk_feeding):
        super().__init__(name, color, weight, height)
        if isinstance(notmilk_feeding, str):
            self.notmilk_feeding = notmilk_feeding
        else:
            raise ValueError('Notmilk_feeding should be str')

    def __str__(self):
        return super(Adjoining, self).__str__() + f'\nnotmilk_feeding:{self.notmilk_feeding}'


adjoining_1 = Adjoining(name='fox', color='ginger', weight=10, height=90, notmilk_feeding='yes')
print(adjoining_1)

print('ZooShow\n''Dolphin show \n' 'Bear show  ')


class Zooshow:

    def ticket(self):
        n = input('Please select the show:')
        if n == "1":
            print('You choice\nDolphin show:There is no such show (price: 100$)')
        elif n == "2":
            return ('You choice\nBear show: rides a bicycle and performs tricks with various objects (price: 70$)')
        else:
            return ('There is no such show')

d = Zooshow()
print(d.ticket())

# class Zooshow:
#     def __init__(self):
#         self.shows = []
#
#     def addShow(self, title, desc, ticket):
#         show = {'title': title, "description": desc, "ticket": ticket}
#
#         self.shows.append(show)
#
#     def chooseShow(self):
#         print('Available shows:', end=" "),
#         cnt = 0
#         for i in self.shows:
#             cnt += 1
#             print(f'{cnt}. {i["title"]}', end=', ')
#         print()
#         choice = int(input("Choose show(type the index number of the show): "))
#
#         for k, v in self.shows[choice-1].items():
#             if k=="ticket":
#                 print(f'{k} - {v} сомов')
#             else:
#                 print(f'{k} - {v}')
#
#     def __str__(self):
#         return f"This zoo has {len(self.shows)} shows"
#
#
# nationalPark = Zooshow()
# nationalPark.addShow("Обезъяны", "Они ездят на велосипедах", 23)
# nationalPark.addShow("Львы", "Львы прыгают на огненном кольце", 60)
#
# print(nationalPark.chooseShow())
