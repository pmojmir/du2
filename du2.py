#Synchronizovat zmanená nahrát na github

import csv

with open("vstup.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ";")
    for row in reader:
        print(row[1])