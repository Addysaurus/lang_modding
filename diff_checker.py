import csv

def check_diff(old_file, new_file, output_file):
    old_entries = []
    new_entries = []
    with open(old_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        for row in reader:
            old_entries.append(row[0:2])
    with open(new_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        for row in reader:
            new_entries.append(row[0:2])
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        header = ['<ID|readonly|noverify>','<English>']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        for i in new_entries:
            if i[0] not in [j[0] for j in old_entries]:
                writer.writerow(i)
            
check_diff('D_units_weaponry.csv', 'DEV_units_weaponry.csv', 'DIFF_units_weaponry.csv')