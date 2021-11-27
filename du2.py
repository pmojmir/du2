import csv #Načtení CSV modulu 

#Vstupní a výstupní data 
vstup = "vstup.csv"
vystup7 = "vystup_7dni.csv"
vystuprok = "vystup_rok.csv"

def kontrola(vstup):
    with open(vstup, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        for row in reader:
            try:
                if float(row[5]) == 0 or float(row[5]) < 0:
                    print((f"{row[4]}.{row[3]}.{row[2]} nulový nebo záporný průtok"))
                elif int(row[4]) > 31 or int(row[4]) <= 0:
                    print((f"{row[4]}.{row[3]}.{row[2]} chybná hodnota v dnu"))
                elif int(row[3]) > 12 or int(row[3]) <= 0:
                    print((f"{row[4]}.{row[3]}.{row[2]} chybná hodnota v měsíci"))
                elif int(row[2]) > 2021 or int(row[2]) < 1980:
                    print((f"{row[4]}.{row[3]}.{row[2]} chybná hodnota v roce"))
            except ValueError:
                pass       
    return()
print(kontrola(vstup))

"""
Funkce zkontroluje vstupy kódy

Argumenty: 
Vstup -- vstupní CSV soubor

Return value:
V případě chybných hodnot upozorní na chybu

"""

def zaokrouhlovani(vstup): 
    vystup = round(vstup,4)
    return (vystup)
"""
Funkce zaokrohlí číslo na čtyři platné číslice 

Argumenty: 
Vstup -- vstupní číselná hodnota 

Return value:
Číslo zaokrouhlené na čtyři desetinné místa

"""
#Část na 7denní průměry, úvod načtení dat a vytvoření souboru pro export dat v modulu CSV 
with open(vstup, encoding="utf-8") as csvfile,\
    open(vystup7, "w", newline='', encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    
    #Počítadlo týdnu a počítadlo řádků
    tyden = 0               #Celkový součet týdnů
    i = 0                   #Počítadlo řádků 
   
    #For cyklus, který prochází jednotlivé řádky
    for row in reader:      
        i = i + 1 
        #Pokud máme 7 hodnotu, zapatujeme si všechny údaje do řádku (nový týden)
        if i % 7 == 1:      
            informace = row[0:4]
        tyden = tyden + float(row[5])   #Průtoky za jednotlivé dny, které se postupně sčítají
        #Pokud je výsledek 0, poslední den týdne 
        if i % 7 == 0:
            prumer7 = (zaokrouhlovani(tyden/7))  #Průměr z týdne
            informace.append(prumer7)            #Přidání do seznamu k datům z prvního dne     
            writer.writerow(informace)           #Zapsání do výstupního csv souboru
            tyden = 0                            #Vynulování týdenních průtoků 
    prumer_dalsi = (tyden/i % 7)                 #Průměr z dalšího týdne 
    writer.writerow([[informace], [(zaokrouhlovani(prumer_dalsi))]]) #Zapsnání do CSV, zaokrouhlení 
print("Hotovo pro sedmidenní průměry")

#Část pro výpočet ročních průtoků, úvod načtení dat a vytvoření souboru pro export dat v modulu CSV  
with open(vstup, encoding="utf-8") as csvfile,\
    open(vystuprok, "w", newline='', encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvfile, delimiter = ",")
    writer = csv.writer(csvoutfile)
    
    #Počítadla řádků (dnů), roků a celkové sumy dnů pro rok
    rok = 0
    suma = 0
    i = 0
    #For cyklus, který prochází jednotlivé řádky
    for row in reader:
        if rok == 0: 
            informace2 = row[0:4]   
        if rok != int(row[2]) and rok !=0: # Definování dalšího roku
            prumer_rok = (zaokrouhlovani(suma/i))
            informace2.append(prumer_rok)
            writer.writerow(informace2)
            suma = 0
            i = 0
            informace2.clear  #Čistění seznamu
            informace2 = row[0:4]
        i = i + 1
        suma = suma + float(row[5])
        rok = int(row[2])             
    prumer_dalsi = (suma/i)
    informace2.append(zaokrouhlovani(prumer_dalsi)) 
    writer.writerow(informace2)
print("Hotovo pro roční průměry")