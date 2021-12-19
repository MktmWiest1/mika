import re
#namber
file_path = 'MOCK_DATA.txt'
file_path1 = 'nambers.txt'

file_read = open(file_path, mode='r', encoding='UTF-8')
final_results = open(file_path1, mode='w', encoding='UTF-8')
class_text = file_read.read()
search = r'#\w+'
result_all = re.findall(search, class_text)

for item in result_all:
    final_results.write(item + '\n')
print(f'total:{str(len(result_all))}')


#допимя
file_path = 'MOCK_DATA.txt'
file_path1 = 'name1.txt'

file_read = open(file_path, mode='r', encoding='UTF-8')
final_results = open(file_path1, mode='w', encoding='UTF-8')
class_text = file_read.read()
search = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9]"
result_all = re.findall(search, class_text)

for item in result_all:
    final_results.write(item + '\n')
print(f'total:{str(len(result_all))}')

#@mail
file_path = 'MOCK_DATA.txt'
file_path1 = 'email.txt'

file_read = open(file_path, mode='r', encoding='UTF-8')
final_results = open(file_path1, mode='w', encoding='UTF-8')
class_text = file_read.read()
search = r'\w+@\w+.[a-z]+'
result_all = re.findall(search, class_text)

for item in result_all:
    final_results.write(item + '\n')
print(f'total:{str(len(result_all))}')

#name
file_path = 'MOCK_DATA.txt'
file_path1 = 'name2.txt'

file_read = open(file_path, mode='r', encoding='UTF-8')
final_results = open(file_path1, mode='w', encoding='UTF-8')
class_text = file_read.read()
search = r'[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+'
result_all = re.findall(search, class_text)
for item in result_all:
    final_results.write(item + '\n')
print(f'total:{str(len(result_all))}')






