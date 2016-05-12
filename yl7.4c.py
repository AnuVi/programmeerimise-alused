'''
Numeroloogias peetakse tähtsaks elutee numbrit, mille arvutamiseks tuleb liita kokku sünnikuupäeva ja -aasta numbrid nii, et jõutakse lõpuks ühe numbrini.

Näiteks, oletame, et sünnikuupäev on 15.05.1975. Teha tuleb niisiis järgnev tehe: 1+5+5+1+9+7+5 = 33, 3+3 = 6, seega on elutee number 6.

Aga kui sünnikuupäevaks on nt. 17.11.1981, siis arvutada tuleb järgmiselt: 1+7+1+1+1+9+8+1 = 29, 2+9 = 11, 1+1=2.

Elutee numbrit arvutab järgmine (rekursiivne) funktsioon, mis võtab argumendiks sünnikuupäeva:
Failis sunnikuupaevad.txt on mingi hulk sünnikuupäevi, iga sünnikuupäev eraldi real. Kirjutada programm, mis tekitab selle faili põhjal 9 tekstifaili nimedega eluteenumber1.txt, eluteenumber2.txt, ..., eluteenumber9.txt ning jagab sünnikuupäevad nendesse failidesse vastavalt elutee numbrile (elutee numbri arvutamiseks kasutada funktsiooni elutee). Näiteks sünnikuupäev 15.05.1975 tuleb kirjutada faili eluteenumber6.txt.
'''
#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))
    
#kuupaevade fail
#kuupaevade_fail = input("Sisestage faili nimi: ")
ava_kuupaevade_fail = open("sunnikuupaevad.txt")
loetud = ava_kuupaevade_fail.readlines()
elutee_numbrid = [1,2,3,4,5,6,7,8,9]
kuupaev_tykk_haaval = []
loodud_failid = []
faili_nimi = "eluteenumber"
laiend = ".txt"
#print(kuupaev)
for rida in loetud:
    kuupaev_tykk_haaval += rida.split()
    for el in kuupaev_tykk_haaval:
        number = elutee(el)
        #print(a)
    
    loodud_failid.append(number)
    uus_fail = open(faili_nimi+str(number)+laiend,'a', encoding="UTF-8")
    uus_fail.write(rida)

for i in elutee_numbrid:
    if(i in loodud_failid):
        i
    else:
        uus_fail = open(faili_nimi+str(i)+laiend,'a', encoding="UTF-8")
   
        


    


