import csv
with open('university_records.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
