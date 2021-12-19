a = [
    {'asd': 123, 'qwe': 432 },
    {'asd': 3, 'qwe': 2}
]
for i  in a:
    print(i)
    if i ['asd'] == 3:
        print(f' мы его нашли! это - {i}')
        a.remove(i)
    else:
        print('netu takogo')

    print(a)

# while True:
#     try:
#        first_number = int(input('введите первое число :'))
#        answer = input('введите знак: + - * / : ')
#        second_number = int(input('введите второе  число :'))
#     except:
#        print('вводите числа !')
#        continue
#     if answer == "+":
#         print(first_number + second_number)23
#
#     elif answer == "-":
#         print(first_number - second_number)
#     elif answer == "*":
#         print(first_number * second_number)
#     elif answer == "/":
#         print(first_number / second_number)
#     else:
#         print("вы вели что то не так!")
# # words = ['python', 'top', 'type']
# # position = input('введите индекс :')
# #
# # try:
# #     words [position]
# # except IndexError:
# #     print('такого индекса нет ')
# except TypeError:
#     print('вводите только целые числа')
