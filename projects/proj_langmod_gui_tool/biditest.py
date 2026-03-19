import re

t = input('Enter text: ')
list1 = re.split(r'([\u0591-\u07FF \s?]+)\s', t)
list2 = [i.strip()[::-1] if re.match(r'[\u0591-\u07FF \s?]', i) else i for i in list1]
[list2.pop(list2.index(i)) for i in list2 if i == '']
print(' '.join(list2))