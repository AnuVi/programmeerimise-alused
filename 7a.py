from urllib.request import urlopen

failveebis = urlopen("https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/mesipuu.txt")
baidid = failveebis.read() #baitidena
text = baidid.decode()
ridadeKaupa = text.splitlines()#reavahetus
failveebis.close()
print(ridadeKaupa[4][7])




