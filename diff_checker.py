import csv

def check_diff(old_file, new_file, output_file):
    old_entries = []
    new_entries = []
    with open(old_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        [old_entries.append(row[0:2]) for row in reader]
    with open(new_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        [new_entries.append(row[0:2]) for row in reader]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        header = ['<ID|readonly|noverify>','<English>']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        for i in new_entries:
            if i[0] not in [j[0] for j in old_entries]:
                writer.writerow(i)
            
check_diff('DEV/DEV_units.csv', 'DEV2/DEV2_units.csv', 'DIFF/DIFF_units.csv')
check_diff('DEV/DEV_units_weaponry.csv', 'DEV2/DEV2_units_weaponry.csv', 'DIFF/DIFF_units_weaponry.csv')
check_diff('DEV/DEV_units_modifications.csv', 'DEV2/DEV2_units_modifications.csv', 'DIFF/DIFF_units_modifications.csv')
check_diff('DEV/DEV_unlocks_attachables.csv', 'DEV2/DEV2_unlocks_attachables.csv', 'DIFF/DIFF_unlocks_attachables.csv')
check_diff('DEV/DEV_menu.csv', 'DEV2/DEV2_menu.csv', 'DIFF/DIFF_menu.csv')
check_diff('DEV/DEV_regional_decals.csv', 'DEV2/DEV2_regional_decals.csv', 'DIFF/DIFF_regional_decals.csv')
check_diff('DEV/DEV_regional_skins.csv', 'DEV2/DEV2_regional_skins.csv', 'DIFF/DIFF_regional_skins.csv')
check_diff('DEV/DEV_unlocks_skins.csv', 'DEV2/DEV2_unlocks_skins.csv', 'DIFF/DIFF_unlocks_skins.csv')