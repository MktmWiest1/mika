import random
from datetime import datetime
from time import sleep
def freez(a):
    for x in a:
        print(x, end="")
        sleep(0.000000000001)
num = random.randint(1, 100)
count = 0
start = input('Хочешь сыграть?\nИгра называется: "Угадай число от 1 до 100\nЕсли хочешь то пиши "Да": ')
freez(
    'Вот тебе подсказски:\n'
    '"очень жарко" +- 5 / '
    '"жарко" +- 10 / '
    '"холодно" +- 30 / '
    '"очень холодно" +30 или -30\n'
    '0 это команда для выхода!\n')
players = input('Введи свое имя:')
while 1:
    try:
        tr = int(input("Сколько попыток хочешь?: "))
        tr = int(tr)
        break
    except ValueError:
        freez("Нужно печатать только целые цифры!\n")
freez("\nИгра уже начался!\nПопробуй теперь угадать цифру!\n")
s = tr
with open('../text.txt', 'a', encoding='UTF-8') as a:
    time_s = datetime.now()
    while count != tr:
        try:
            guess = int(input())
        except ValueError:
            freez("Нужно печатать только целые цифры!\n")
            continue
        if guess == 0:
            freez("Программа завершена!\nСпасибо за то-что играл в мою игру!❤️\nСоздатель игры Мактым 🎮")
            break
        if guess == num:
            count += 1
            freez(f'Ты выиграл!\nСпасибо за то-что играл в мою игру!❤️\nСоздатель игры Мактым 🎮')
            a.write(f'\nИмя игрока: {players}😈🔥\n')
            freez(f'\nУгадано за {count} попыток!')
            time_f = datetime.now() - time_s
            a.write(f'Ты начал в: {time_s.strftime("%X")} \n')
            a.write(f'Ты закончил в: {datetime.now().strftime("%X")} \n')
            a.write(f'Вы хотели {tr} попыток\nУгадано с {count}-попытки!\nВаше время - {time_f.seconds} секунд\n')
            break
        elif guess <= num + 5 and guess >= num - 5:
            count += 1
            if guess < num:
                freez("очень жарко, выше⬆️\n")
            elif guess > num:
                freez("очень жарко, ниже⬇️\n")
        elif guess <= num + 10 and guess >= num - 10:
            count += 1
            if guess < num:
                freez("жарко, выше⬆️\n")
            elif guess > num:
                freez("жарко, ниже⬇️\n")
        elif guess <= num + 30 and guess >= num - 30:
            count += 1
            if guess < num:
                freez("холодно, выше⬆️\n")
            elif guess > num:
                freez("холодно, ниже⬇️\n")
        elif guess < (num + 30) and guess > 0 or guess > (num + 30) and guess <= 100:
            count += 1
            if guess < num:
                freez("очень холодно, выше⬆️\n")
            elif guess > num:
                freez("очень холодно, ниже⬇️\n")
        else:
            freez('Пишите только от 1 до 100\n')
        s -= 1
        freez(f'У вас ещё есть {s} попыток\n')
    if count == tr:
        freez(f'\nВаши попытки закончились!\nЦель был {num}\nСпасибо за то-что играл в мою игру!❤️\nСоздатель игры Мактым 🎮‍')