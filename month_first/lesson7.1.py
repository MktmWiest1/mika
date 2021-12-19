from random import choice
from datetime import datetime
from time import sleep

start = datetime.now()
print(start)
sleep(5)
print((datetime.now() - start).seconds)
print(datetime.now())

def timer (seconds):
  while seconds != 0:
    sleep(1)
    print(seconds)
    seconds -= 1
timer(10)

# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student}')
#     asked.append(student)
#     print(asked)
#
# print(students)



