import re

t = "מרכז שיקום ואחזקה 7000 / רפאל מערכות לחימה מתקדמות | (Samson Remote Controlled Weapon Station 30mm) נגמ״ש מרכבה"
list1 = re.split(r'([\u0591-\u07FF \s?]+)\s', t)
list2 = [i.strip()[::-1] if re.match(r'[\u0591-\u07FF \s?]', i) else i for i in list1]
for i in list2:
    if i == '':
        list2.pop(list2.index(i))
print(' '.join(list2))