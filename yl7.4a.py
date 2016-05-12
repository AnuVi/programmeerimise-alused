'''
Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad ja ülejäänute kohta ei ole midagi teada. Peo eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja programmi, mis arvutab

maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale) ja
minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba seda teatanud).
Esmalt koostada funktsioon eelarve, mis võtab argumendiks külaliste arvu tähistava täisarvu ning arvutab ja tagastab selle põhjal eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105.

Programm

küsib kasutajalt failinime;
loeb sellest failist informatsiooni külaliste kohta;
arvutab ja väljastab ekraanile kutsutud inimeste arvu;
arvutab ja väljastab ekraanile inimeste arvu, kes on juba tulemisest teatanud;
arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud funktsiooni eelarve;
arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud funktsiooni eelarve.
'''

def soogi_eelarve(osalejate_arv):
    sook = 10 * osalejate_arv
    return sook

def rent():
    return 55

def eelarve(osalejate_arv):
    s = soogi_eelarve(osalejate_arv)
    r = rent()
    kokku = r+s
    return kokku

faili_nimi = input("Sisestage faili nimi: ")
fail = open(faili_nimi, encoding="UTF-8")
loetud = fail.readlines()
kutsutud = 0
tulijad = 0
kahtlejad = 0

for rida in loetud:
    kutsutud +=1
    nimi = rida.split() #yks tulija
    for s in nimi:
        if (s[0]=="+"):
            tulijad +=1

max_eelarve = eelarve(kutsutud)
min_eelarve = eelarve(tulijad)

print("Kutsutud on " + str(kutsutud) + " inimest.")
print(str(tulijad) +" inimest tuleb.")
print("Maksimaalne eelarve " + str(max_eelarve) + " eurot")
print("Minimaalne eelarve " + str(min_eelarve) + " eurot")