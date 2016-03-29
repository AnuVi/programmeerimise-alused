ainepunktid = int(input("Siseta ainepunktide arv täisarvuna: "))
nadalate_arv = int(input("Sisesta nädalate arv täisarvuna: "))
ajakulu_ainepunktidele = ainepunktid * 26
yhe_nadala_ajakulu = ajakulu_ainepunktidele/nadalate_arv
print(round(yhe_nadala_ajakulu))