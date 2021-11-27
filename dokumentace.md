Dokumentace k domácímu úkolu číslo 2. 

*****
Zadání
*****
Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidenní průměry. Program bude neinteraktivní.

*****
Vstup
*****

Program načte CSV s průměrnými denními průtoky zvolené řeky ze souboru pojmenovaného vstup.csv. Testovací data jsou stažena ze stránek ČHMÚ a jedná se o stanici na řece Klavaba v obci Nový Huť na Plzeňsku. Soubor se jmenuje vstup.csv

*****
Výstup
*****

Výstupem jsou dva soubory ve formátu csv, které se jmenejí vystup_7dni.csv a vystup_rok.csv

vystup_7dni.csv = představuje sedmidenní průměry vstupních dat, datum bude uvedeno vždy prvního dne z úseku, který se průměruje, průtok bude průměrem průtoků prvního až sedmého dne úseku, zaokrouhleným na 4 číslice za desetinnou tečkou.

vystup_rok.csv = obsahuje roční průměry vstupních dat

Pokud jsou vstupní data chybná, uživatel bude upozorněn, kde se nachází chybná hodnota, jako např. nulový průtok 