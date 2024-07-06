import csv


def save_to_csv(data, filepath):
    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)
