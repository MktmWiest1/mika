class Car:
    def __init__(self, brand, power, speed, color,
                 transmission, cost):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string')
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Power should be int')
        if isinstance(power, float):
            self.power = power
        else:
            raise ValueError('Speed should be int')
        if isinstance(speed, int):
            self.speed = speed
        else:
            raise ValueError('Speed should be int')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(transmission, str):
            self.transmission = transmission
        else:
            raise ValueError('Transmission should be string')
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError('Cost should be integer')

    def tunning(self, cost_of_tunnig):
        summery = cost_of_tunnig + self.cost
        return f'Final cost of car is {summery}'

    def __str__(self):
        return f'brand:{self.brand}\n' \
               f'power: {self.power}\n' \
               f'speed: {self.speed}\n' \
               f'color: {self.color}\n' \
               f'transmission: {self.transmission}\n' \
               f'cost: {self.cost}$'


car_1 = Car(brand='Lexus 570', power=5.7, speed=240,
            color='Black', transmission='automat', cost=12000)
print(car_1)
print(car_1.tunning(56765))

class Hybrid(Car):
      def init(self, brand, power, speed, color,
               transmission, cost, capacity_electricity):
            super().__init__(brand, power, speed, color,
                             transmission, cost)
            if isinstance(capacity_electricity, int):
                self.cap = capacity_electricity

            else:
                raise ValueError('cap should be integer')
      def economy_fuel(self, day, costing):
          summary = day * costing
          return f'Your econom cost : {summary}'

      def __str__(self):
          return super(Hybrid, self).__str__() + f'\nCapacity :{self.cap}'

hybrid_1 = Hybrid(brand='Lexus 450h', power=4.7, speed= 300,
            color='Silver', transmission='automat', cost=90500,)
print(hybrid_1)
