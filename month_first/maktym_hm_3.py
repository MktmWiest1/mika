# Дан кортеж состоящий из разных типов данных:
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1,' G' )
# Создать два пустых списка letters и numbers
letters = []
numbers = []
# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
for l in data_tuple:
    if type(l) == str:
     letters.append(l)
    else:
     numbers.append(l)
print(letters)
print(numbers)
# Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
numbers.remove(numbers[0])
print(numbers)
p = numbers.pop(0)
letters.append(p)
print(numbers)
print(letters)
numbers.insert(1,2)
print(numbers)
# Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
numbers.sort()
print(numbers)
letters.reverse()
print(letters)
# Преобразовать списки numbers и letters в кортежи
numbers = tuple(numbers)
letters = tuple(letters)
print(numbers)
print(letters)