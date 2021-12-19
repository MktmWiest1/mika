ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*ten_list)
evens = []
for i in ten_list:
    if i % 2 == 0:
        evens.append(i)
print(*evens)
evens2 = []
for i in evens:
    i = i * i
    evens2.append(i)
print(*evens2)
def ten(lst=ten_list):
    while 1:
        try:
            num = input("Введите индекс числа: ")
            if num == 'q':
                break
            else:
                print(lst[int(num)])
        except Exception:
            print(f"индекс: от 0 до {len(lst)-1}\n")
g = [2,3,3,4,4,2,3,32,3]
ten(g)