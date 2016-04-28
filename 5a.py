# Järjendi loomine
nädalapäevad = ["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev", "pühapäev"]
 
# Järjendi saab ekraanil väljastada
print(nädalapäevad)
 
# Elementide arvu (järjendi pikkuse) leidmine
nädalapäevi = len(nädalapäevad)
print('Järjendis ' + str(nädalapäevi) + ' elementi')
 
# Järjendisse kuulumise kontroll
if "palgapäev" in nädalapäevad:
    print("Palgapäev on järjendis")
else:
    print("Palgapäev ei ole järjendis")
 
# Konkreetse elemendi väärtus indeksi (järjekorranumbri) abil
print(nädalapäevad[1])

a = ['A', 'B', 'C', 'D', 'E']
#kogu järjend algusest lõpuni
print(a[:])
#kogu järjend algusest - B-ni
print(a[0:2])
#alati viimane
print(a[-1])


fail = open("andmed.txt", encoding="UTF-8")
for rida in fail:
    print("Lugesin sellise rea: " + rida)
fail.close()