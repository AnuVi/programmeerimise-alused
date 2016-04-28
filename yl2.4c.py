import math

inimesed  = int(input("Inimeste arv: "))
kohad = int(input("Kohtade arv: "))

mitu_bussi = math.ceil(inimesed/kohad)
inimesi_viimases = inimesed%kohad

if(inimesi_viimases == 0):
    inimesi_viimases = kohad


print("Inimeste arv: " + str(inimesed) )
print("Kohtade arv: " + str(kohad) )
print("Busse vaja: " + str(mitu_bussi) )
print("Viimases bussis inimesi " + str(inimesi_viimases) )