from easygui import *

nimi = enterbox("Tere, mis on sinu nimi?")
vanus = integerbox("Kui vana te olete?", lowerbound = 1, upperbound = 120)

if nimi == None or vanus == None or nimi == "":
    msgbox("Palun sisestage andmed korrektselt!")
else: msgbox("Tere, " + str(vanus) + "-aastane " + nimi + "!")