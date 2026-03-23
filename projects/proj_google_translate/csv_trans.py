import asyncio, csv, time
from googletrans import Translator, LANGCODES

async def translate_csv_all_lang(input_file, output_file):
    original_entries = []
    translated_entries = []
    
    with open(input_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        [original_entries.append(row[0:2]) for row in reader]
        
    async with Translator() as translator:
        for i in original_entries[891:917]:
            start_time = time.perf_counter()
            temp = i[1]
            num = 1
            for j in LANGCODES:
                temp = await translator.translate(temp, dest=j)
                temp = temp.text
                print(str(num) + '. ' + temp)
                num += 1
            temp = await translator.translate(temp, dest='en')
            temp = temp.text
            print(temp)
            temp_list = [i[0], temp]
            translated_entries.append(temp_list)
            end_time = time.perf_counter()
            print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        header = ['<ID|readonly|noverify>','<English>']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        for i in translated_entries:
            writer.writerow(i)
        
asyncio.run(translate_csv_all_lang('DEV2/DEV2_units.csv', 'projects/proj_google_translate/TRANS_units.csv'))