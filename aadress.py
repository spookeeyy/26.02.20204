from easygui import *
nimi = enterbox("Palun sisesta oma nimi: ")
vanus = integerbox("Palun sisesta oma vanus: ", lowerbound = 1, upperbound = 150)
aadress = enterbox("Palun sisesta oma aadress: ")

failinimi = filesavebox()

f = open(failinimi, "w")
f.write(nimi + "\n")
f.write(str(vanus) + "\n")
f.write(aadress + "\n")
f.close()

d