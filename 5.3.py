#Koostada programm, mis
#loeb failist nimega konto.txt andmed;
#väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud.
#Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks
#nagu failis.

fail = open("konto.txt")
for rida in fail:
    sissetulek = float(rida)
    if sissetulek > 0:
        print(sissetulek)
