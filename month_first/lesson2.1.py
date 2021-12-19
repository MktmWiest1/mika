# ----for

'''for i in range(1, 5):
  print(i, end='')'''

'''counter = 0

while counter != 10:
  counter += 1
  print(counter)
'''

# color = 'red'
# color = 'off'

'''
while True:
  color = input("svetofor color: ")
  if color == 'red':
    print("stop")
  elif color == 'green':
    print("go")

  else:
    print('look at situation')
    break
'''
'''
apples = 10
good_apples = 0
bad_apples = 0

while apples != 0:
  apples = apples - 1
  answer = input('good or bad: ')

  if answer == 'good':
    good_apples = good_apples + 1
  else: 
    bad_apples = bad_apples + 1

  print(" ")
  print("apples: {}".format(apples))
  print("good apples {}".format(good_apples))
  print("bad apples {}".format(bad_apples))
'''

'''rounds = 0

while 1:
  rounds = rounds + 1
  print(rounds)
  if rounds == 3:
    print('next')
    continue
  elif rounds == 5:
    print('stop')
    break
'''

# for letter in 'Django':
#     if letter == 'D' or letter == 'g':
#         continue
#     print("current letter: " + letter)