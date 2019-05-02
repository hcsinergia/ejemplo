#!/usr/bin/python -tt
from Tkinter import *

def setMyText():
	v.set("Hola")

frame = Frame()
button=Button(frame, text="Button", command=setMyText)
button.pack(side=LEFT)

v = StringVar()
text = Entry(frame, textvariable=v)
text.pack(side=LEFT);

frame.pack()
frame.mainloop()