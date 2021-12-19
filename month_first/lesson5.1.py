numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
words = {}

c = 0
while c != len(numbers):
    words =[numbers[c]]=letters[c]
    print(words)
    c += 1
print(words)


# b = dict(zip(numbers, letters))
# print(b)


# univer = []
# tehnikum = []
# army = []
# abiturient = [
#     {'name': "akylai", 'OPT': 105, 'gender': 'female'},
#     {'name': "dastan", 'OPT': 120, 'gender': 'male'},
#     {'name': "meerim", 'OPT': 99, 'gender': 'female'},
#     {'name': "askar", 'OPT': 0, 'gender': 'male'}
# ]
# abiturient1 = [
#     {'name': "aziza", 'OPT': 105, 'gender': 'female'},
#     {'name': "beka", 'OPT': 120, 'gender': 'male'},
#     {'name': "nurai", 'OPT': 99, 'gender': 'female'},
#     {'name': "aslan", 'OPT': 0, 'gender': 'male'}
# ]
#
# def all_abiturient(list):
#     for i in abiturient:
#         for k, v in i.items():
#             print(f'{k}: {v}')
#         print(' ')
#
# all_abiturient(abiturient1)
#
# def seleccion(lst, u, t, a):
#     for i in lst:
#         if i['OPT'] >= 105:
#             u.append(i)
#         elif i['OPT'] < 105 and i ['OPT'] > 0:
#             t.append(i)
#         elif i['OPT'] == None and i['gender'] == 'male':
#             a.append(i)
#
#
# seleccion(abiturient, univer, tehnikum, army)
# print('u', univer)
# print('t', tehnikum)
# print('a', army)

# def menu(**kwargs):
#     return kwargs
# monday  = menu(breakfast ='яичница', lunch = 'bivshteks', dinner = 'pelmeni')
# print(monday)

# def numbers(a,*args):
#     # print(args)
#     return  a + sum(args)
#
#
# print(numbers(2, 3, 4, 5, 6, 7))

# def square(a,b,c=4):
#     print(a+b+c)
#     return a+b+c
# #quare(input(int ('введите ширину ')),int (input('введите высоту')))
# # our = square(4, 6, 5)
# print(square(4,6,5) - square(2,3,5)
#
# print(type(our))
