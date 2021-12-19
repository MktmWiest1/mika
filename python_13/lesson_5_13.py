import re
my_text = 'Vasya 1964 vasya@gmail.com %1000$ ' \
          'Adilet 1997 adilet@intel.com %1000$ ' \
          'Aidana 2000 aidana@gmail.com &1000$ ' \
           'Erbol 2001 lilbol@yendex.com *1000$ ' \
           'Alia 2003 alia@gmail,com %1000$ '

'''
\d = 0-9 Any digit
\D = Any non digit
\w = [A-Z a-z]
\W = non alphabet symbol
s\ = breakspace
S\ = None breakspace

'''

file_path = 'class_mock_data.txt'
result_file_path = 'results.txt'

file_read = open(file_path, mode='r', encoding='Latin-1')
final_results = open(result_file_path, mode='w', encoding='Latin-1')
class_text = file_read.read()
search = r'@\w+.\w+.[a-z]+'
result_all = re.findall(search, class_text)

for item in result_all:
    print(item)
    final_results.write(item + '\n')
print(f'total:{str(len(result_all))}')

# search = r'[%*&][0-9]+[$]'
# results_all = re.findall(search, my_text)
# print(results_all)


