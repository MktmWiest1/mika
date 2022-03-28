# students = ['Aziia' , 'Asel' , 2, 10, True, numbers ]
# numbers = list()

# print(type(students))
mentor = ['Эсенбек', 'Мирхад', 'Беки']
while True:
    command = input(f'{mentor} \n'
                    f'Выберите команду: \n'
                    f'1 - добавление \n'
                    f'2 - изменение \n'
                    f'3 - удаление \n'
                    f'4 - выход \n')
    if command == '1':
        new_mentor = input('\nВведите имя ментора,которого вы хотитете добавить:').capitalize()
        if new_mentor in mentor:
            print("этот ментор уже есть в списке")
            if len(mentor) <= 5:
                print("нельзя больше добавлять")
            elif len(new_mentor) <= 15:
                mentor.append(new_mentor)
            else:
                print('\n Имя должно содержать не более 15 букв')
                continue
    if command == '2':
        changed_mentor = input('\n Введите имя ментора,которого вы хотите заменить:').capitalize()
        added_mentor = input('\n Введите имя нового ментора:').capitalize()
        if changed_mentor in mentor and len(added_mentor) <= 15:
            mentor.remove(changed_mentor)
            mentor.append(added_mentor)
        elif changed_mentor in mentor and len(added_mentor) >= 15:
            print('\n Имя должно содержать не более 15 букв')
            continue
        else:
            print('\n Ментора,которого вы хотите изменить,нет в списке')
            continue

    if command == '3':
        b = input('Выберите способ по которому будем удалять по индексу или по имени n/i?')
        if b == 'n':
            g = input('Введите имя').capitalize()
            if g in mentor:
                mentor.remove(g)
            else:
                print("Этого ментора нету в списке")
                continue
        elif b == 'i':
            f = int(input('Введите индекс'))
            if f > len(mentor) - 1:
                print('Этого индекса нет')
                continue
            else:
                del mentor[f]
    if command == '4':
        print(f'finish{tuple(mentor)}')
    break

    # elif command == '2':
    # print('редактируем')
    # elif command == '0':
    # print('finish')
    # break

    # mentors = 5
    # for i in range(len(mentors)) :
    print(i)
