from random import randint
ise = input("Kui soovite ise valida kummal tribüünil istuda, siis sisesage 'ise': ")


ise = ise.lower()
tribyyn = "Pilet on "
pohjatribyyn = "põhjatribüünile"
lounatribyyn = "lõunatribüünile"

#kui loosiga
if(ise!="ise"):
    
    intro = "Pilet loositi. "
    suvaline_arv = randint(1,3)
    
    if(suvaline_arv!=1):
        tribyyn = tribyyn + lounatribyyn
    else:
        tribyyn = tribyyn + pohjatribyyn
        
else:
    intro = "Valisite ise. "
    pohi = input("Kui soovite põhjatribüünile, siis sisestage 'p': ")
    pohi = pohi.lower()
    
    if(pohi!="p"):
        tribyyn = tribyyn + lounatribyyn
    else:
        tribyyn = tribyyn + pohjatribyyn


print(intro + tribyyn)