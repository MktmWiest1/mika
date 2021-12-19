import re

new_file = 'MOCK_DATA (2).txt'
file1 = 'Name.txt'
file2 = 'Info.txt'
file3 = 'Gmail.txt'
file4 = 'Numbers.txt'

r = open(new_file,'r', encoding='UTF-8')
w1 = open(file1,'w',encoding='UTF-8')
w2 = open(file2,'w',encoding='UTF-8')
w3 = open(file3,'w',encoding='UTF-8')
w4 = open(file4,'w',encoding='UTF-8')

text = r.read()
search1 = r'[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+'
search2 = r'[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9]'
search3 = r'\w+@\w+.[a-z]+'
search4 = r'#\w+'
results1 = re.findall(search1,text)
results2 = re.findall(search2,text)
results3 = re.findall(search3,text)
results4 = re.findall(search4,text)

for item in results1:
    w1.write(item + '\n')
    w2.write(item + '\n')
    w3.write(item + '\n')
    w4.write(item + '\n')
print(f'Total:{len(results1)}')
print(f'Total:{len(results2)}')
print(f'Total:{len(results3)}')
print(f'Total:{len(results4)}')