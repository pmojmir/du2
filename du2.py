import csv
from os import R_OK

#Funkce na zaokrouhlení na 4 platné číslice 
def zaokrouhlovani(vstup): 
    vystup = round(vstup,4)
    return (vystup)

#Kód na 7denní průměry 
with open("Klabava.csv", encoding="utf-8") as csvfile,\
    open("vystup_7dni.csv", "w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    #print(next(reader))
    tyden = 0
    i = 0 
    for row in reader:
        i += 1
        if i % 7 == 1:
            id = row[0]
            qd = row[1]
            rok = row[2]
            mesic = row[3]
            den = row[4]
        tyden += float(row[5])
        if i % 7 == 0:
            prumer7 = (zaokrouhlovani(tyden/7))
            informace = (id, qd, rok, mesic, den, prumer7)
            writer.writerow(informace)
            tyden = 0 
    prumer_dalsi = (tyden/i % 7)        
    writer.writerow([[informace], [(zaokrouhlovani(prumer_dalsi))]])
print("Hotovo")


