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
    
def translit_hebrew(text):
    transliteration_dict = {
        'א' : "'",
        'ב' : 'v',
        'בּ' : 'b',
        'ג' : 'g',
        'ד' : 'd',
        'ה' : 'h',
        'הּ' : 'h',
        'ו' : 'v',
        'וּ' : 'u',
        'וֹ' : 'o',
        'ז' : 'z',
        'ח' : 'ḥ',
        'ט' : 'ṭ',
        'י' : 'y',
        'כ' : 'kh',
        'ך' : 'kh',
        'כּ' : 'k',
        'ךּ' : 'k',
        'ל' : 'l',
        'מ' : 'm',
        'ם' : 'm',
        'נ' : 'n',
        'ן' : 'n',
        'ס' : 's',
        'ע' : "'",
        'פ' : 'f',
        'ף' : 'f',
        'פּ' : 'p',
        'ףּ' : 'p',
        'צ' : 'ṣ',
        'ץ' : 'ṣ',
        'ק' : 'k',
        'ר' : 'r',
        'ש' : 's',
        'שׂ' : 's',
        'שׁ' : 'š',
        'ת' : 't',
        '׳' : "'",
        'ַ' : 'a',
        'ָ' : 'a',
        'ֵ' : 'e',
        'ֶ' : 'e',
        'ִ' : 'i',
        'ֹ' : 'o',
        '◌ֻ' : 'u',
        'ַ' : 'a',
        'ְ' : '',
        'ׇ' : 'o',
        'ֳ' : 'o',
        'ֱ' : 'e'
    }
    
    text_list = list(text)
    final_list = []
    for i in text_list:
        if i in transliteration_dict.keys():
            final_list.append(transliteration_dict[i])
        elif i == '.' or i == ' ' or i in ['1', '2', '3', '4', '5', '6', '7', '0', '9', '0']:
            final_list.append(i)
    print(final_list)
    print(''.join(final_list))

while True:
    choice = input('''Select what operation you would like to perform:
                
    1. Russian transliteration
    2. Hebrew transliteration
                   
    E. Exit

    Enter your choice: ''')

    if choice == '1':
        text = input('Enter the Russian text you would like to transliterate: ')
        translit_russian(text)
    elif choice == '2':
        text = input('Enter the Hebrew text you would like to transliterate: ')
        translit_hebrew(text)
    elif choice.upper() == 'E':
        break