from easygui import *

nupud = ["lihtne", "ok", "keeruline"]
vajutati = buttonbox("Programmerimine on ", choices = nupud)
if vajutati == "keeruline":
    msgbox("õpi rohkem")
else:
    msgbox("Te arvate, et programmeerimine on " + vajutati + "!")
