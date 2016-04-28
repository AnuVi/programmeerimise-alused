nimi = input("Sisestage Leedu perekonnanimi: ")
#ei lõppe e-ga
if(nimi[-1]!="e"):
    print("Pole ilmselt leedulanna perekonnanimi")
else:
    if(nimi[-2]!="t" and nimi[-2]!="n" ):
        print("Määramata")
    elif(nimi[-2]=="t"):
        print("Vallaline")
    else:
        print("Abielus")
