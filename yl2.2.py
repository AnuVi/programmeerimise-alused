pikkus = int(input("Sisesta pikkus: "))
kaelakaart = input("Kas kasutaja omab kaelakaarti? ")
pilet = input("Kas kasutaja omab piletit? ")


kaelakaart = kaelakaart.lower()
pilet = pilet.lower()

if (pikkus < 120 and (kaelakaart=="jah" or pilet=="jah")):
    print("Pääseb allveelaevale")
else:
    print("Ei pääse allveelaevale")

    