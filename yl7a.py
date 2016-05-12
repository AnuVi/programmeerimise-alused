'''
Kirjutada programm, mis
küsib kasutajalt failinime,
loeb vastavast failist sõnumi ja
väljastab selle ekraanile telegrammi stiilis. Teha tuleb asendused
Ä, ä → AE
Õ, õ, Ö, ö → OE
Ü, ü → UE
Kõik tähed tuleb muuta suurtähtedeks.
Teisi märke ei muudeta.
'''

failiNimi = input("Sisestage failinimi: ")
fail = open(failiNimi, encoding="UTF-8")
loetud = fail.read()
loetud = loetud.upper()
loetud = loetud.replace("Ä", "AE")
loetud = loetud.replace("Õ","OE")
loetud = loetud.replace("Ö","OE")
loetud = loetud.replace("Ü", "UE")

print(loetud)
    
