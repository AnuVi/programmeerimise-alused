#On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv {lilli. Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.
#Koostada programm, mis
#küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
#arvutab for-tsükli ja funktsiooni range() abil lillede koguarvu, mida pood kingib;
#väljastab saadud lillede arvu ekraanile.

arv = int(input("Sisesta ostjate arv: "))
lillede_arv = 0
paaritud = []
#leiame paaritud arvud
for i in range(1, arv+1, 2):
    #paarisarv
    print(i)
    paaritud.append(i)
#leiame suurima paaritu arv
lillede_arv = sum(paaritud)

        
print("Lillede koguarv on " + str(lillede_arv) + ".")