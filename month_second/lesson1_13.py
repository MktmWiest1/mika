class Human:
    # name ='Maktym'
    # age = 18
    # gender = 'female'
    def __init__(self, name, age, gender,lan):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('age should be integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('gender should be integer')
        if isinstance(lan, str):
            self.lan = lan
        else:
            raise ValueError('lan should be string')


      # self.name = name
      # self.age = age
      # self.gender = gender
      # self.lang = lan

    def can_say_name(self):
        return f'My name is {self.name}'
    def my_lang(self):
        return f'I speak in {self.my_lang}'


    def __str__(self):
        return f' Age: {self.age}\n ' \
               f' Name:{self.name}\n '\
               f' Gender:{self.gender}\n'\
               f' Lag:{self.lan}\n'\




humen_1 = Human( age=18,name='maktym', gender='female', lan ='russ' )
humen_2 = Human( age=28,name='mak', gender='male', lan='japan')
print(humen_1.can_say_name(), humen_1.my_lang())
print(humen_2.can_say_name(),humen_1.my_lang())
print(humen_1)
print(humen_2)



