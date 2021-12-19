nominal = [20, 50, 100, 500, 1000, 2000, 5000]
personal = [
           'Т Молдо', 'К Датка', 'Т Сатылганов ', 'А Осмонов', \
            'С Каралаев', 'Ж Баласагын', 'Манас', 'С Чокморов',
           ]

banknotes = dict(zip(nominal, personal))


# for i,l in banknotes.items():
#     print(f'{i} :{l}')
# print(banknotes)

# next_month = []
# data = [
#     {
#          'name': "adilet",
#          'points': 40,
#          'test':60,
#         'StandUp': True
#     },
#     {
#          'name': "adina",
#          'points': 30,
#          'test':45,
#         'StandUp':False
#     },
# ]
# c = 0
# while c != len (data):
#     for i in data:
#         c += 1
#         #for k in i :
#         if i ['points'] >=40 and i ['test'] >= 60 and i ['StandUp']== True :
#             next_month.append(i)
#         else:
#             print(i['name'], 'Не проходит!')
# print(next_month)


# plov = {'мясо','рис','морковь'}
# kuurdak= {'мясо', 'картофель', 'лук'}

# print(plov.intersection (kuurdak))
# print(plov& kuurdak)
#
# print(plov.difference (kuurdak))
# print(plov -  kuurdak)
#
# print(plov.symmetric_difference (kuurdak))
# print(plov ^ kuurdak)
#
# print(plov.union(kuurdak))
# print(plov | kuurdak)


# a = [1, 2, 3, 1, 3]
# a = set(a)
# set_1 = {'abc', 'oop', 'abc'}
# print(set_1)
# print(a)
