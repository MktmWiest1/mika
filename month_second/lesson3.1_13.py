class Phone:
    def __init__(self, name, cost, color, memory, cpu, camera, size):
        self.name = name
        self.cost = cost
        self.color = color
        self.memory = memory
        self.cpu = cpu
        self.camera = camera
        self.size = size

    def call_to_someone(self, number):
        return f'This phone calling to this number: {number}'

    def __str__(self):
        return f'Name of Product:{self.name}\n' \
               f'Cost: {self.cost}\n' \
               f'Color: {self.color}\n' \
               f'Memory: {self.memory}GB\n' \
               f'CPU: {self.cpu}Gigahertz\n' \
               f'Camera: {self.camera}PX\n' \
               f'Size: {self.size}\n'


class IPhone(Phone):
    def __init__(self, name, cost, color, memory, cpu, camera, size):
        super().__init__(name, cost, color, memory, cpu, camera, size)

    def info(self):
        if self.name == 'IPone 13':
            return f'Best camera at the moment'
        elif self.name == 'IPhone 5':
            return f'Legend Desing of Apple phones'
        elif self.name == 'IPhone 6':
            return f'Awful desing'

    def __str__(self):
        return super(IPhone, self).__str__()


iphone_13 = IPhone('IPhone 13', '1200', 'red', '1024', 2.4, 16, 3.4, )
iphone_5 = IPhone('IPhone 5', '800', 'silver', '64', 1.6, 4, 2.0, )
print(iphone_13)
print(iphone_5)
print(iphone_5.info())
print(iphone_13.info())












