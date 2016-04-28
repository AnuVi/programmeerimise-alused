# sõnet saab panna ka """ Kolmekordsetesse "", '' """ märkidesse
print("""Kolmekordsetesse "", ''""")
print ('''Kolmekordsetesse "", '' ''')


# print käsku saab teha nii
algus = "\n \n Selles lauses on"
arv = 4
lopp = "sõna!"
print(algus + str(4)+lopp)
#aga ka nii
print(algus, arv, lopp)

#väljastab tehte
print("sõna"*5)

#suur algustäht
print("\nsõna".capitalize())

#kontrollib,kas sõna lõpeb "tu"-ga: true/false 
print("\nsõna".endswith("tu"))

#kontrollib,kas sõna algab "tu"-ga: true/false 
print("\nsõna".startswith("tu"))

#esitähe teeb suureks
print("\nsõna on laural".title())




