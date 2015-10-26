#Geschreven door: Christiaan Ileana, Studentnummer: 1674596, Klas: ICT-V1G

import random
import csv

#=========================================== Sectie =======================================================

#Maak database file aan en definieer de functies
csvfile = open("data.csv", "a")
f = csv.writer(csvfile, delimiter = ";")

csvfile2= open("data.csv", "r")
f2 = csv.DictReader(csvfile2, delimiter = ";")


#Dictionary met keuzes voor bagagekluis
optie = {
        1: "Ik wil een nieuwe kluis",
        2: "Ik wil mijn kluis openen",
        3: "Ik geef mijn kluis terug",
        4: "Ik wil weten hoeveel kluizen er nog vrij zijn"
        }

#Laat gebruiker keuzemenu zien
def optiemenu():
        print("Welkom bij de NS Bagagekluis...\n")
        for i in optie:
            print(i, "-", optie[i])
        print("")

optiemenu()

#=========================================== Sectie =======================================================

#definieer gebruiker I/O
def optie_1():
    i = 0
    pin = random.randrange(1000,9999)
    for c in f2:
        i += 1
    if i < 12:
        a = i + 1
        print("Uw pincode is:", pin)
        f.writerow((a, pin))
    else:
        print("Helaas, de kluizen zijn op..")


def optie_2():
    b = input("Geef hier uw pincode op: ")
    for row in f2:
        if b in row["code"]:
            print("Uw kluisnummer is:", row["kluis"])


def optie_3():
    print("Ga naar het CSV bestand en verwijder hem zelf")


def optie_4():
    row = 0
    aantal = 12
    for i in f2:
        row += 1
    print("Het aantal beschikbare kluizen is:", (aantal - row))

#=========================================== Sectie =======================================================

#Vraag gebruiker om de keuze
def keuze():
    keuze = input("Uw keuze nummer: ")
    return keuze

a = keuze()


#Definieer wat de keuze moet doen
def user_input():
    if a == "1":
        optie_1()
    elif a == "2":
        optie_2()
    elif a == "3":
        optie_3()
    elif a == "4":
        optie_4()
    else:
        print("Verkeerde invoer...\n")

user_input()

csvfile.close()
csvfile2.close()
