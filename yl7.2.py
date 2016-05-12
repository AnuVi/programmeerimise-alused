'''
Kirjutada programm, mis

küsib kasutaja käest ühe sissekande (võib eeldada, et sissekanne on ilma reavahetusteta);
kirjutab (UTF-8 kodeeringus) faili paevik.txt lõppu kolm rida:
esimesel real praegune kuupäev ja kellaaeg sellisel kujul, nagu seda tagastab funktsioon datetime.today() (vt näidet);
teisel real kasutaja sisestatud kirje;
tühi rida (pole kohustuslik).
'''

from datetime import datetime
kuupaev_kellaaeg = datetime.today()

kanne = input("Sisestage sissekande tekst:")
fail = open("paevik.txt",'a', encoding="UTF-8")
loetud = fail.read()
print(loetud)
fail.write('\n' + str(kuupaev_kellaaeg))
fail.write('\n' + kanne)
fail.write('\n' )
fail.close()
