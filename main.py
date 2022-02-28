'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''
import random

gondolt_szam = random.randint(1,5)
#print(gondolt_szam)

szam = int(input('Adj meg a egy számot! '))
if szam == gondolt_szam:
    print(szam)
    print("Eltaláltad!")
else:
    print(szam)
    print("Nem jó válasz.")
    print(gondolt_szam)
    print("Ez volt a jó válasz.")
