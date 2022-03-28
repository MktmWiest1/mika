class Cattle: #Крупный рогатый скот
    def __init__(self, name, wight, size, horn, sex):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name should be str")
        if isinstance(wight, float):
            self.wight = wight
        else:
            raise Exception("Wight should be float")
        if isinstance(size, str):
            self.size = size
        else:
            raise ValueError("Size should be str")
        if isinstance(horn, bool):
            self.horn = horn
        else:
            raise ValueError("Horn should be bool")
        if isinstance(sex, str):
            self.sex = sex
        else:
            raise ValueError("Sex should be str")

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Wight: {self.wight}kg\n" \
               f"Size: {self.size}\n" \
               f"Horn: {self.horn}\n" \
               f"Sex: {self.sex}"


class Bull(Cattle):
    def __init__(self, name, wight, size, horn, sex):
        super().__init__(name, wight, size, horn, sex)

    def gives_meat(self, pet):
        return f"This {pet} gives meat"

    def __str__(self):
        return super(Bull, self).__str__()
bull = Bull(name="Ferdinant", wight=1100.5,
                size="Large", horn=True, sex="Male")

print(bull)
print(bull.gives_meat("Bull"))
print("---"*10)

class Cow(Cattle):
    def __init__(self, name, wight, size, horn, sex):
        super().__init__(name, wight, size, horn, sex)

    def gives_milk(self, pet):
        return f"This {pet} gives meat"

    def __str__(self):
        return  super(Cow, self).__str__()

cow = Cow(name="Murka", wight= 720.5,
          size="middle", horn=True, sex="Female")
print(cow)
print(cow.gives_milk("Cow"))
print("---"*10)

class Calf(Bull, Cow): #Теленок
    def __init__(self, name, wight, size, horn, sex):
        super().__init__(name, wight, size, horn, sex)

    def info(self):
        if self.sex == "Male":
            return f"If pet male he gives meat"
        elif self.name == "Female":
            return f"If pet female he gives milk "
    def __str__(self):
        return super(Calf, self).__str__()


calf = Calf(name="Mishka", wight=25.5,
            size="small", horn=False, sex="male or female")
print(calf)
print(calf.info())
print(calf.gives_milk("if calf female"))
print(calf.gives_meat("If calf male"))
print("---"*10)

# Задание № 2 Множественное Наследование ( Один ко многим )
class Simcard():
    def __init__(self, name, cost, color, postal_code, e_mail, contact_center, generation):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name should be str")
        if isinstance(cost, str):
            self.cost = cost
        else:
            raise ValueError("Cost should be str")
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color should be str")
        if isinstance(postal_code, int):
            self.postcod= postal_code
        else:
            raise Exception("Postal ccode should be int")
        if isinstance(e_mail, str):
            self.mail = e_mail
        else:
            raise ValueError("E-mail should be str")
        if isinstance(contact_center, int):
            self.contact = contact_center
        else:
            raise Exception("Contact center must be int")
        if isinstance(generation, int):
            self.gen = generation
        else:
            raise Exception("Generation must be int ")

    def use_internet(self, operator):
        return f"You can use internet with the help of:{operator}"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Cost: {self.cost}\n" \
               f"Color: {self.color}\n" \
               f"Postal code: {self.postcod}\n" \
               f"E-mail: {self.mail}\n" \
               f"Contact center: *{self.contact}\n"