'''
NB! Kui ülaltoodud aadressilt andmeid ei saa kätte (nt Macide kasutajad), siis palun proovida http://kodu.ut.ee/~eno/mooc/jaanuar jt.

Kirjutada programm, mis

küsib kasutajalt kuunime (võib eeldada, et kasutaja sisestab kuunime õigesti ja "märts" asemel kirjutab "marts"),
küsib kasutajalt päeva (võib eeldada, et sisestatud kuus leidub sellise järjekorranumbriga päev),
loeb vastavalt aadressilt selle kuu nimepäevad (kasulik oleks nendest koostada järjend, abiks võib olla meetod splitlines()) ja
väljastab ekraanile sisestatud kuupäevale vastavad nimepäevalised.
'''

from urllib.request import urlopen

kuu = input("Sisestage kuu: ")
paev = int(input("Sisestage päev: "))
intro = "Kuupäeval" + str(paev) + ". " + kuu + " on nimepäevad järgmiste nimedega inimestel: " + "\n"
adr = "http://kodu.ut.ee/~eno/mooc/" + kuu
fail_veebis = urlopen(adr)
baidid = fail_veebis.read() # kogu fail baitidena
tekst = baidid.decode() # baitidest saab sõne
ridade_kaupa = tekst.splitlines()
see_rida = (ridade_kaupa[paev-1])
fail_veebis.close()
print(intro + see_rida)