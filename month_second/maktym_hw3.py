# 1. Создать 4 класса и с помощью их преобразить РОМБОВИДНЫЙ
# тип множественного наследования
# 2. У супер класса должны быть не меньше 4 атрибутов
# 3. У каждого класса должно быть не меньше 2 методов
# 4. Также должны быть соблюдены def __str__(self) + super()
# 5. И к каждому классу создать объект ( в итоге будет не меньше 4
# объектов )
class Family:  # ромбовидный
    def __init__(self, name, gender, height, work):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender should be string')

        if isinstance(height, int):
            self.height = height
        else:
            raise ValueError('height should be int')

        if isinstance(work, str):
            self.work = work
        else:
            raise ValueError('work should be string')

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Sex:{self.gender}\n' \
               f'Height:{self.height}\n' \
               f'Work:{self.work}\n'


class Father(Family):
    def __init__(self, name, gender, height, work):
        super(Father, self).__init__(name, gender, height, work)

    def can_defend(self, family):
        return f"Defend {family}"

    def __str__(self):
        return super(Father, self).__str__()


fat = Father(name='Den', gender='male', height=180, work='Yes')
print(fat)
print('--' * 15)


class Mather(Family):
    def __init__(self, name, gender, height, work):
        super(Mather, self).__init__(name, gender, height, work)

    def can_defend(self, family):
        return f"Defend {family}"

    def __str__(self):
        return super(Mather, self).__str__()


mat = Mather(name='Anne', gender='female', height=160, work='Yes')
print(mat)
print('--' * 15)


class Son(Father, Mather):
    def __init__(self, name, gender, height, work, age):
        super().__init__(name, gender, height, work)
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be integer')

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Sex:{self.gender}\n' \
               f'Height:{self.height}\n' \
               f'Work:{self.work}\n' \
               f'Age:{self.age}\n'

    def can_defend(self, family):
        return f"Defend {family}"


son1 = Son(name='Aian', gender='male', height=170, work='no', age=15)
print(son1)
print('-*' * 15)


# Задание № 2 Множественное Наследование ( Один ко многим )
# 1. Создать 4 класса , один из них является супер-классом , от которого
# наследуются все остальные 3 класса
# 2. У супер класса должно быть как минимум 4 атрибута ( def __init__(self, atribut,
# atribut2): )
# 3. У каждого класса должно быть как минимум 2 метода ( def method(self): )
# 4. Также должны быть соблюдены def __str__(self) + super()
# 5. К каждому классу создать по одному объекту ( в итоге должно быть 4
# объекта )

class Feline:
    def __init__(self, name, weight, height, kinds):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string')

        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('Weight should be int')

        if isinstance(height, int):
            self.height = height
        else:
            raise ValueError('Height should be int')

        if isinstance(kinds, str):
            self.kinds = kinds
        else:
            raise ValueError('Kinds should be str')

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Weight:{self.weight}kg\n' \
               f'Height:{self.height}sm\n' \
               f'view:{self.kinds}\n'


feline1 = Feline(name='Puma', weight=105, height=180, kinds='predator')
print(feline1)
print('--' * 15)


class Leo(Feline):
    def __init__(self, name, weight, height, kinds, gender):
        super(Leo, self).__init__(name, weight, height, kinds)

        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender should be string')

    def __str__(self):
        return super(Leo, self).__str__() + f'Gender:{self.gender}\n'


feline2 = Leo(name='lion', weight=250, height=200, kinds='Panthera leo', gender='male')
print(feline2)

class Tiger(Feline):
    def __init__(self, name, weight, height, kinds, gender):
        super(Tiger, self).__init__(name, weight, height, kinds)

        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender should be string')

    def __str__(self):
        return super(Tiger, self).__str__() + f'Gender:{self.gender}\n'

