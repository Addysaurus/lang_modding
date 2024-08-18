def translit_russian(text):
    ru_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'І', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ў', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    en_translit = ['A', 'B', 'V', 'G', 'D', 'Ye', 'Ë', 'Ž', 'Z', 'I', 'J', 'Ì', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'Ŭ', 'F', 'Kh', 'Cz', 'Č', 'Š', 'Ŝ', '"', 'Y', "'", 'È', 'Û', 'Â']
    text_list = list(text)
    final_list = []
    for i in text_list:
        if i.isupper():

            final_list.append(en_translit[ru_alphabet.index(i)])
        elif i.islower():
            final_list.append(en_translit[ru_alphabet.index(i.upper())].lower())
        else:
            final_list.append(i)
    print(final_list)
    for i in final_list:
        if i == 'Cz':
            if final_list.index(i) > 0 and final_list[final_list.index(i) - 1] not in ['I', 'i', 'E', 'e', 'Y', 'y', 'J', 'j']:
                i = 'C'
        elif i == 'cz':
            if final_list.index(i) > 0 and final_list[final_list.index(i) - 1] not in ['I', 'i', 'E', 'e', 'Y', 'y', 'J', 'j']:
                i = 'c'
    print(final_list)
    final_name = ''.join(final_list)
    print(final_name)

repeat = True

while repeat:
    choice = input('''Select what operation you would like to perform:
                
    1. Russian transliteration
                   
    E. Exit

    Enter your choice: ''')

    if choice == '1':
        text = input('Enter the Russian text you would like to transliterate: ')
        translit_russian(text)
    elif choice.upper() == 'E':
        repeat = False