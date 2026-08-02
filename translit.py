import re

def translit_russian(text):
    translit_dict = {
        'А' : "A",
        'Б' : 'B',
        'В' : 'V',
        'Г' : 'G',
        'Д' : 'D',
        'Е' : ['Ye', "'E"],
        'Ё' : ['Yo', "'O"],
        'Ж' : 'Ž',
        'З' : 'Z',
        'И' : ['I', "'I"],
        'Й' : 'J',
        'К' : 'K',
        'Л' : 'L',
        'М' : 'M',
        'Н' : 'N',
        'О' : 'O',
        'П' : 'P',
        'Р' : 'R',
        'С' : 'S',
        'Т' : 'T',
        'У' : 'U',
        'Ф' : 'F',
        'Х' : 'Kh',
        'Ц' : 'Ts',
        'Ч' : 'Ch',
        'Ш' : 'Sh',
        'Щ' : "Sh'",
        'Ъ' : '"',
        'Ы' : 'Y',
        'Ь' : "'",
        'Э' : 'E',
        'Ю' : ['Yu', "'U"],
        'Я' : ['Ya', "'A"]
    }

    voice_pair = {
        'П': 'Б',
        'Ф': 'В',
        'К': 'Г',
        'Т': 'Д',
        'Ш': 'Ж',
        'С': 'З'
    }

    devoice_pair = {v : k for k, v in voice_pair.items()}

    paired_voiced = set(devoice_pair.keys())  # Б В Г Д Ж З
    paired_voiceless = set(voice_pair.keys()) # П Ф К Т Ш С
    unpaired_voiceless = {'Х', 'Ц', 'Ч', 'Щ'}

    def preserve_case(original, replacement):
        return replacement if original.isupper() else replacement.lower()

    def assimilate_clusters(text):
        chars = list(text)
        pattern = r'[БВГДЖЗПФКТШСХЦЧЩбвгджзпфктшсхцчщ]+'

        for m in re.finditer(pattern, text):
            start, end = m.span()
            cluster = chars[start:end]

            # Find the controlling final obstruent, ignoring В (V)
            obstruent_final = None

            for j in range(len(cluster) - 1, -1, -1):
                c = cluster[j].upper()
                obstruent_final = c
                break

            # If the entire cluster is just В/в
            if obstruent_final is None:
                continue

            if obstruent_final in paired_voiced:
                mode = "voice"
            else:
                mode = "devoice"

            for j in range(len(cluster) - 1):
                c = cluster[j]
                u = c.upper()
                
                if mode == "voice":
                    if u in voice_pair:
                        chars[start + j] = preserve_case(c, voice_pair[u])
                else:
                    if u in devoice_pair:
                        chars[start + j] = preserve_case(c, devoice_pair[u])
        return ''.join(chars)

    def devoice_v(text):
        # В --> Ф before a voiceless obstruent.
        chars = list(text)

        for i in range(len(chars) - 1):
            if chars[i].upper() != 'В':
                continue
            nxt = chars[i + 1].upper()
            if nxt in paired_voiceless or nxt in unpaired_voiceless:
                chars[i] = preserve_case(chars[i], 'Ф')
        return ''.join(chars)

    def final_devoicing(text):
        chars = list(text)

        for m in re.finditer(r'[БВГДЖЗбвгджз]\b', text):
            i = m.start()
            c = chars[i]
            if chars[i - 1].isalpha():
                chars[i] = preserve_case(c, devoice_pair[c.upper()])
        return ''.join(chars)

    def apply_russian_voicing(text):
        text = assimilate_clusters(text)
        text = devoice_v(text)
        text = final_devoicing(text)
        return text
    
    def translit(text):
        modified_voicing = list(apply_russian_voicing(text))
        print(modified_voicing)
        final_translit = []
                
        for idx, i in enumerate(modified_voicing):
            if i.upper() not in translit_dict:
                final_translit.append(i)
                continue

            if i.upper() in {'Е', 'Ё', 'И', 'Ю', 'Я'}:
                if re.search(r'[БВГДЗПФКТСХЧбвгдзпфктсхч]', modified_voicing[idx - 1]):
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][1].upper())
                    else:
                        final_translit.append(translit_dict[i.upper()][1].lower())
                elif re.search(r'[Щщ]', modified_voicing[idx - 1]):
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][1][1:].upper())
                    else:
                        final_translit.append(translit_dict[i.upper()][1][1:].lower())
                elif modified_voicing[idx - 1].upper() == 'Ь':
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][1][1:].upper())
                    else:
                        final_translit.append(translit_dict[i.upper()][1][1:].lower())
                else:
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][0])
                    else:
                        final_translit.append(translit_dict[i.upper()][0].lower())
                continue

            mapping = translit_dict[i.upper()]
            final_translit.append(mapping if i.isupper() else mapping.lower())
        
        print(final_translit)
        print(''.join(final_translit))
        
    translit(text)
    
def translit_ukrainian(text):
    translit_dict = {
        'А' : "A",
        'Б' : 'B',
        'В' : 'V',
        'Г' : 'Gh',
        'Ґ' : 'G',
        'Д' : 'D',
        'Е' : 'E',
        'Є' : ['Ye', "'E"],
        'Ж' : 'Ž',
        'З' : 'Z',
        'И' : 'Y',
        'Й' : 'J',
        'І' : ['I', "'I"],
        'Ї' : 'Yi',
        'К' : 'K',
        'Л' : 'L',
        'М' : 'M',
        'Н' : 'N',
        'О' : 'O',
        'П' : 'P',
        'Р' : 'R',
        'С' : 'S',
        'Т' : 'T',
        'У' : 'U',
        'Ф' : 'F',
        'Х' : 'Kh',
        'Ц' : 'Ts',
        'Ч' : 'Ch',
        'Ш' : 'Sh',
        'Щ' : "Shch",
        'Ь' : "'",
        'Ю' : ['Yu', "'U"],
        'Я' : ['Ya', "'A"]
    }

    voice_pair = {
        'П': 'Б',
        'Ф': 'В',
        'Х': 'Г',
        'К': 'Ґ',
        'Т': 'Д',
        'Ш': 'Ж',
        'С': 'З',
        'Ч': 'Дж',
        'Ц': 'Дз'
    }

    devoice_pair = {v : k for k, v in voice_pair.items()}

    paired_voiced = set(devoice_pair.keys())  # Б В Г Д Ж З
    paired_voiceless = set(voice_pair.keys()) # П Ф К Т Ш С
    unpaired_voiceless = {'Х', 'Ц', 'Ч', 'Щ'}

    def preserve_case(original, replacement):
        return replacement if original.isupper() else replacement.lower()

    def assimilate_clusters(text):
        chars = list(text)
        pattern = r'[БВГДЖЗПФКТШСХЦЧЩбвгджзпфктшсхцчщ]+'

        for m in re.finditer(pattern, text):
            start, end = m.span()
            cluster = chars[start:end]
            obstruent_final = None
            
            for j in range(len(cluster) - 1, -1, -1):
                c = cluster[j].upper()
                if c == 'В':
                    continue
                obstruent_final = c
                break

            if obstruent_final is None:
                continue

            # Regressive voicing, but not regressive devoicing
            if obstruent_final in paired_voiced:
                for j in range(len(cluster) - 1):
                    c = cluster[j]
                    u = c.upper()

                    if u in voice_pair:
                        chars[start + j] = preserve_case(c, voice_pair[u])
        return ''.join(chars)

    def apply_ukrainian_voicing(text):
        text = assimilate_clusters(text)
        return text
    
    def translit(text):
        modified_voicing = list(apply_ukrainian_voicing(text))
        print(modified_voicing)
        final_translit = []
        
        for idx, i in enumerate(modified_voicing):
            if i.upper() not in translit_dict:
                final_translit.append(i)
                continue

            if i.upper() in {'Є', 'І', 'Ю', 'Я'}:
                if re.search(r'[БВГДЗПФКТСХЧЩбвгдзпфктсхчщ]', modified_voicing[idx - 1]):
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][1].upper())
                    else:
                        final_translit.append(translit_dict[i.upper()][1].lower())
                elif modified_voicing[idx - 1].upper() == 'Ь':
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][1][1:].upper())
                    else:
                        final_translit.append(translit_dict[i.upper()][1][1:].lower())
                else:
                    if i.isupper():
                        final_translit.append(translit_dict[i.upper()][0])
                    else:
                        final_translit.append(translit_dict[i.upper()][0].lower())
                continue

            # Determining whether В is pronounced as a V or a W.
            if i.upper() == 'В':
                if (
                    idx == len(modified_voicing) - 1
                    or re.search(
                        r'[БВГДЖЗЙПФКТСХЧШЩбвгджзйпфктсхчшщ]',
                        modified_voicing[idx + 1]
                    )
                ):
                    final_translit.append('W' if i.isupper() else 'w')
                else:
                    final_translit.append('V' if i.isupper() else 'v')
                continue

            mapping = translit_dict[i.upper()]
            final_translit.append(mapping if i.isupper() else mapping.lower())
        
        print(final_translit)
        print(''.join(final_translit))
        
    translit(text)
          
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

while True:
    choice = input('''Select what operation you would like to perform:
                
    1. Russian transliteration
    2. Ukrainian transliteration
    3. Hebrew transliteration
                   
    E. Exit

    Enter your choice: ''')

    if choice == '1':
        text = input('Enter the Russian text you would like to transliterate: ')
        translit_russian(text)
    elif choice == '2':
        text = input('Enter the Ukrainian text you would like to transliterate: ')
        translit_ukrainian(text)
    elif choice == '3':
        text = input('Enter the Hebrew text you would like to transliterate: ')
        translit_hebrew(text)
    elif choice.upper() == 'E':
        break