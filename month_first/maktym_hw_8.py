# #Создать программу “Таблица умножения”.
# Программа должна запрашивать у пользователя имя и количество попыток.
# Затем работать в бесконечном цикле до истечения указанных попыток.
# Программа должна запрашивать произведение двух случайных чисел от 1 до 9.
# После ввода пользователем ответа, выводить на экран правильный ответ.
# Каждый вопрос-ответ записывать в файл results.txt
# В этот же файл дописать итоговый отчёт с указанием имени, количества попыток и затраченного времени.
import random
import time

name = input('Таблица умножения😊\nВведите имя:')
attemps = int(input("Сколько попыток хочешь?: "))
timesec = time.time()

print(name, attemps)

showattemps = attemps

while attemps != 0:
    attemps -= 1
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    userInput = int(input(f'{num1} * {num2} = ? '))
    correct = num1 * num2

    if userInput == correct:
        print(f'Правильно!\nОтвет - {correct}')
        with open('../resultstabl.txt', 'a', encoding='UTF-8') as a:
            a.write(f"{num1} * {num2} ={correct} Правильно\n")

    else:
        print(f'Неправильно!\nОтвет - {correct}')
        with open('../resultstabl.txt', 'a', encoding='UTF-8') as a:
            a.write(f"{num1} * {num2} ={correct} Неравильно \n")
    print(f'Осталось {attemps} попыток!\n')

print(f'Имя игрока: {name}\nПопыток: {showattemps}\nВремя: - {round(time.time() - timesec)} секунд\n ')
with open('../resultstabl.txt.txt', 'a', encoding='UTF-8') as a:
    a.write(f'Имя игрока: {name}\nПопыток:{showattemps}\nВремя: - {round(time.time() - timesec)} секунд\n')
