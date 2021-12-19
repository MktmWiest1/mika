from random import randint
cash = 500
while cash > 0:
    try:
        bet = int(input(f'введите ставку: доступно - {cash} '))
    except:
        print('вводите только числа')
        continue
    if bet > cash or bet < 1:
        print(f'ставка не должна быть больше {cash} или меньше 0')
        continue
    comp = randint(1, 6)
    user = randint(1, 6)
    print(f'программа: {comp}, у вас: {user}')

    if comp > user:
        print('Вы проиграли')
        cash -= bet
        print(cash)
        with open('results.txt', 'a', encoding ='utf-8') as file:
            file.write(f'k:{comp}, ю:{user}Ставка : {bet} Проигрыш: {cash - bet} Остаток {cash}')
    elif comp < user:
        print('Вы выиграли')
        comp += bet
        print(cash)
        with open('results.txt', 'a',encoding ='utf-8') as file:
            file.write(f'\nk:{comp}, ю:{user}Ставка : {bet} Выгрыш: {cash - bet} Остаток {cash}')
    else:
        print('Ничья')
        print(cash)
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(f'\nk:{comp}, ю:{user}Ставка : {bet} Ничья: {cash - bet} Остаток {cash}')



# file = open('text.txt', 'r', encoding="utf - 8")
# print(file.read())
#
# file .close()

# with open('words.txt', 'w') as text: # перезапись
#     text.write('hello World ')
#
# with open ('words.txt', 'a') as text: # доплнительная запись
#     text.write('\nmy name is jhon')
#
# with open('words.txt', 'r') as gymn:# чтение
#     print(gymn.read())
