from pythainlp.transliterate import transliterate

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
        'ק' : 'ḳ',
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
    
def translit_thai(text):
    # engine = 'iso_11940'
        # -*- coding: utf-8 -*-
    # SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
    # SPDX-License-Identifier: Apache-2.0
    """
    Transliterating Thai text using ISO 11940

    :See Also:
        * `Wikipedia \
            <https://en.wikipedia.org/wiki/ISO_11940>`_
    """
    _consonants = {
        "ก": "k",
        "ข": "k̄h",
        "ฃ": "ḳ̄h",
        "ค": "kh",
        "ฅ": "k̛h",
        "ฆ": "ḳh",
        "ง": "ng",
        "จ": "j",
        "ฉ": "c̄h",
        "ช": "ch",
        "ซ": "s",
        "ฌ": "c̣h",
        "ญ": "ỵ",
        "ฎ": "ḍ",
        "ฏ": "ṭ",
        "ฐ": "ṭ̄h",
        "ฑ": "ṯh",
        "ฒ": "t̛h",
        "ณ": "ṇ",
        "ด": "d",
        "ต": "t",
        "ถ": "t̄h",
        "ท": "th",
        "ธ": "ṭh",
        "น": "n",
        "บ": "b",
        "ป": "p",
        "ผ": "p̄h",
        "ฝ": "f̄",
        "พ": "ph",
        "ฟ": "f",
        "ภ": "p̣h",
        "ม": "m",
        "ย": "y",
        "ร": "r",
        "ฤ": "v",
        "ล": "l",
        "ฦ": "ł",
        "ว": "w",
        "ศ": "ṣ̄",
        "ษ": "s̛̄",
        "ส": "s̄",
        "ห": "h̄",
        "ฬ": "ḷ",
        "อ": "x",
        "ฮ": "ḥ",
    }

    _vowels = {
        "ะ": "a",
        "ั": "ạ",
        "า": "ā",
        "ำ": "å",
        "ิ": "i",
        "ี": "ī",
        "ึ": "ụ",
        "ื": "ụ̄",
        "ุ": "u",
        "ู": "ū",
        "เ": "e",
        "แ": "æ",
        "โ": "o",
        "ใ": "ı",
        "ไ": "ị",
        "ฤ": "v",
        "ฤๅ": "vɨ",
        "ฦ": "ł",
        "ฦๅ": "łɨ",
        "ย": "y",
        "ว": "w",
        "อ": "x",
    }

    _tone_marks = {
        "่": "–̀".replace("–", ""),
        "้": "–̂".replace("–", ""),
        "๊": "–́".replace("–", ""),
        "๋": "–̌".replace("–", ""),
        "็": "–̆".replace("–", ""),
        "์": "–̒".replace("–", ""),
        "–๎".replace("–", ""): "~",
        "–ํ".replace("–", ""): "–̊".replace("–", ""),
        "–ฺ".replace("–", ""): "–̥".replace("–", ""),
    }

    _punctuation_and_digits = {
        # ฯ can has two meanings in ISO 11940.
        # If it is for abbrevation, it is paiyan noi.
        # If it is for sentence termination, it is angkhan diao.
        # Without semantic analysis, they cannot be distinguished from each other.
        # In this simple implementation, we decided to always treat ฯ as paiyan noi.
        # We commented out angkhan diao line to remove it from the dictionary
        # and avoid having duplicate keys.
        "ๆ": "«",
        "ฯ": "ǂ",  # paiyan noi: U+01C2 ǂ Alveolar Click; ICU uses ‡ (double dagger)
        "๏": "§",
        # "ฯ": "ǀ",  # angkhan diao: U+01C0 ǀ Dental Click; ICU uses | (vertical bar)
        "๚": "ǁ",  # angkhan khu: U+01C1 ǁ Lateral Click; ICU uses || (two vertical bars)
        "๛": "»",
        "๐": "0",
        "๑": "1",
        "๒": "2",
        "๓": "3",
        "๔": "4",
        "๕": "5",
        "๖": "6",
        "๗": "7",
        "๘": "8",
        "๙": "9",
    }

    _all_dict = {
        **_consonants,
        **_vowels,
        **_tone_marks,
        **_punctuation_and_digits,
    }
    _keys_set = _all_dict.keys()


    def transliterate(word: str) -> str:
        """
        Use ISO 11940 for transliteration
        :param str text: Thai text to be transliterated.
        :return: A string indicating how the text should be pronounced, according to ISO 11940.
        """
        _str = ""
        for i in word:
            if i in _keys_set:
                _str += _all_dict[i]
            else:
                _str += i
        return _str
    print(transliterate(text))

while True:
    choice = input('''Select what operation you would like to perform:
                
    1. Russian transliteration
    2. Hebrew transliteration
    3. Thai transliteration
                   
    E. Exit

    Enter your choice: ''')

    if choice == '1':
        text = input('Enter the Russian text you would like to transliterate: ')
        translit_russian(text)
    elif choice == '2':
        text = input('Enter the Hebrew text you would like to transliterate: ')
        translit_hebrew(text)
    elif choice == '3':
        text = input('Enter the Thai text you would like to transliterate: ')
        translit_thai(text)
    elif choice.upper() == 'E':
        break