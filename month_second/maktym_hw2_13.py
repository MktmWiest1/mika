# Задача №1 Наследование
# 1. Создать трехступенчатую концепцию (дед-отец-ребенок) любого примера который вам ближе
# 2. Все три класса должны иметь свои особенные методы и атрибуты как минимум два доп метода у каждого класса
# 3. Также создать хотя бы по одному объекту к каждому класс
class Cinema:
    def __init__(self, name, year_of_issue, genre):
        self.name = name
        self.year_of_issue = year_of_issue
        self.genre = genre

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Year_of_issue: {self.year_of_issue}\n' \
               f'Genre: {self.genre}\n'


c_1 = Cinema('Hachiko', "2017", 'drama, family, foreign')
print(c_1)


class TVseries(Cinema):
    def __init__(self, name, year_of_issue, genre, time, language):
        super(TVseries, self).__init__(name, year_of_issue, genre)
        self.time = time
        self.language = language

    def __str__(self):
        return super(TVseries, self).__str__() + f'Time: {self.time}\n' \
                                                 f'Language: {self.language}\n'


c_2 = TVseries("Mech", "2009", "Thriller", "120 min", "Russ")
print(c_2)


class Series(TVseries):
    def __init__(self, name, year_of_issue, genre, time, language, interpreter, color):
        super(Series, self).__init__(name, year_of_issue, genre, time, language)
        self.interpreter = interpreter
        self.color = color

    def __str__(self):
        return super(Series, self).__str__() + f'Interpreter: {self.interpreter}\n' \
                                               f'Color: {self.color}\n'


seria = Series("Imper KI", "2013", "Romantic", "45", "Korea", 'Russ', 'yes')
print(seria)


# Задача №2 Инкапсуляция
# 1. Создать один класс в котором вы пропишете по одному методу (внутреннего и защищенного)
# 2. В этом классе должно быть также по одному атрибуту (внутреннего и защищенного)

class Education:
    def _math(self):
        print('This is an internal method of the object')


study = Education()
study._math()
print('_' * 30)


class Education:
    def __init__(self):
        self.__math = 'Archimedes'


study = Education()


# Задача № 3 Полиморфизм без наследования
# 1. Создать три разных класса в котором будут одинаковые методы по названию например (attack)
# 2. Но логика этого самого метода будут разные как в случае примера с мечником , лучник

class Archer:
    def __init__(self, attack):
        self.attack = attack

    def greeting(self):
        return f'Archer'


class Swordsman:
    def __init__(self, attack2):
        self.attack2 = attack2

    def greeting(self):
        return f'Sword skill'


class Мagician:
    def __init__(self, attack1):
        self.attack1 = attack1

    def greeting(self):
        return f'Ability to use magic'


a = Archer('french')
m = Мagician('english')
s = Swordsman('japanese')
print(a.greeting())
print(m.greeting())
print(s.greeting())

# Задача № 4 Полиморфизм с наследованием
# 1. Все тоже самое как в случае с Полиморфизмом без наследование , единственное различие здесь присутствует наследование

print("adam" + "adahan")

a = 'Показывать время и дату'


class Nokia_1:
    def notify(self):
        print(f'{a} черно-белом экране')


class Nokia_2(Nokia_1):
    def notify(self):
        print(f'{a} цветном экране')


class Nokia_3(Nokia_2):
    def notify(self):
        print(f'{a} в живом обои ')


band3 = Nokia_1()
band3.notify()

band4 = Nokia_2()
band4.notify()
