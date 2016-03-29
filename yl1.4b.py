nimi = input("Sisesta oma nimi: ")
lubatud_kiirus = int(input("Sisesta lubatud kiirus täisarvuna: "))
tegelik_kiirus = int(input("Sisesta tegelik kiirus täisarvuna: "))
trahv = (tegelik_kiirus-lubatud_kiirus)*3

if (trahv > 190):
    trahv = min (190, trahv)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")





