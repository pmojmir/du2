#Synchronizovat zmanená nahrát na github
#Úvod
import csv

#Import CSV
with open("park.csv", encoding="utf-8") as csvinfile,\
    open("park_out.csv", "w", encoding="utf-8") as csvoutfile: