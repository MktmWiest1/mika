# --------lists

# data_types = ['hello', 'name', 123, 5, True, False, 2.5, 3.9]
# strings = list()
#
# print(len(data_types))
# strings = list('12345')
# data_types.append(strings)
# data_types.extend(strings)

# print(data_types[0])
# print(data_types[0:4])
# print(data_types[0:4:3]) #вывод через каждый третий элем

# data_types.append('abc')
# data_types.insert(1, 25)
# data_types += '100'
# strings.append(data_types[0:4])

# print(strings)
# print(data_types)

# data_types.clear()
# data_types.remove('name')
# deleted = data_types.pop(-1)
# strings.append(data_types.pop(-1))
# strings.append(data_types.pop(-1))
# del data_types[0], data_types[3]

# data_types[0] = 'goodbie'

# print(data_types)
# print(deleted)
# print(strings)

'''
for i in data_types:
  if type(i) == str:
  #if i == 'hello' or i == 'name' :
    strings.append(i)
  else:
    print(i)

print(data_types)
print(strings)'''
'''
for i in range(1, 5+1):
  strings.append(i)

print(strings)
'''

# while len(strings) != 5:
#     word = input("Type something: ")
#     strings.append(word)
#     print(strings)
#
# print(strings)