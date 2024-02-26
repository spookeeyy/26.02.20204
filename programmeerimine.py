from easygui import *

variandid = ["minu lemmik", "lihtne", "ok", "keeruline"]
vajutati = choicebox("Programmeerimine on ", choices = variandid)
if vajutati == None:
    msgbox("Te ei valinud midagi!")
elif vajutati == "minu lemmik":
    msgbox("Programmeerimine on teie lemmik! Muidugi nii peakski olema!")
else:
    msgbox("Te arvate, et programmeerimine on ", + vajutati + ", hmm, väga huvitav!")