"""
Ada tahab minna reisile ja uurib viimase hetke pakkumisi. Võimalikud sihtkohad on kirjas failis (iga sihtkoht on eraldi real). Faili võite salvestada siit või koostada ise mõne tekstiredaktoriga.

Koostada programm, mis

küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt sihtkohad.txt);
loeb sisestatud nimega failist andmed;
näitab kõik sihtkohad koos järjekorranumbritega (alates 1);
küsib kasutajalt, mitmes sihtkoht broneerida (kasutaja sisestab alati täisarvu);
väljastab ekraanile vastavalt valitud arvule sihtkoha.
"""

failinimi = input("Palun sisestage failinimi:")
fail = open(failinimi)
sihtkohad = []
txt = ["Võimalikud sihtkohad: ", "Valige mitmes sihtkoht broneerda: ", "Reis broneeritud. Sihtkoht on "]
jrk_nr = 1

#faili küsimine
print(txt[0])

#loeme andmed sisse
for rida in fail:
    sihtkohad.append(rida)
    #jrk number
    print (str(jrk_nr) + ". " + rida)
    jrk_nr +=1
fail.close()
    
#mitmes sihtkoht
mitmes = int(input(txt[1]))

#asukoht
asukoht = sihtkohad[mitmes-1]

print("\n" + txt[2] + asukoht[:-2]+'.')


    
    
