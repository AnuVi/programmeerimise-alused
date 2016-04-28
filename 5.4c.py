"""
Koostada programm, mis

küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal on vähemalt 31 nime);
loeb sisestatud nimega failist andmed;
väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema.
"""
from datetime import *
today = (datetime.now().day)
opilased = []

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi)

for rida in fail:
    opilased.append(rida)

#lucky winner
opilane = opilased[today-1]
print (opilane)

    
fail.close()