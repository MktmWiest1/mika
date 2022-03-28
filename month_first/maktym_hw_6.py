# ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*ten_list)
# evens = []
# for i in ten_list:
#     if i % 2 == 0:
#         evens.append(i)
# print(*evens)
# evens2 = []
# for i in evens:
#     i = i * i
#     evens2.append(i)
# print(*evens2)
# def ten(lst=ten_list):
#     while 1:
#         try:
#             num = input("Введите индекс числа: ")
#             if num == 'q':
#                 break
#             else:
#                 print(lst[int(num)])
#         except Exception:
#             print(f"индекс: от 0 до {len(lst)-1}\n")
#
#
# ten()


# lamda функция


# ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# events = list(filter(lambda x: x % 2 == 0, ten))
# print(events)
#
# events = list(map(lambda x: x ** 2, events))
#
# print(events)
#
#
# def obj(lst=ten):
#     while 1:
#         try:
#             num = int(input("Введите индекс числа: "))
#             if num == 88:
#                 break
#
#             else:
#                 print(lst[num])
#         except Exception:
#             print(f"Введите правильный индекс числа:\nиндекс: от 0 до {len(lst) - 1}\n")
#
# obj()
#
# print(ten)
