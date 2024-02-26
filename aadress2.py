from easygui import *
failinimi = fileopenbox()
f = open(failinimi)

nimi = f.readline().strip()
vanus = f.readline().strip()
aadress = f.readline().strip()

f.close()

tekst = "Nimi: "+nimi+"\n"+"Vanus: "+vanus+" aastat\n"+"Aadress: "+aadress

msgbox(tekst)