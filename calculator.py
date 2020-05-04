#!/usr/bin/env python3

from tkinter import *
window = Tk()

# bufferExpression = [] 
bufferString = ""

def digit(value):
	global bufferString
	bufferString += value
	print(bufferString)

def input_key(param):
	print (param + " has been inputed")
	digit(param)

Button(window, text="0", command=lambda: input_key("0")).pack()
Button(window, text="1", command=lambda: input_key("1")).pack()
Button(window, text="2", command=lambda: input_key("2")).pack()
Button(window, text="3", command=lambda: input_key("3")).pack()
Button(window, text="4", command=lambda: input_key("4")).pack()
Button(window, text="5", command=lambda: input_key("5")).pack()
Button(window, text="6", command=lambda: input_key("6")).pack()
Button(window, text="7", command=lambda: input_key("7")).pack()
Button(window, text="8", command=lambda: input_key("8")).pack()
Button(window, text="9", command=lambda: input_key("9")).pack()
Button(window, text="+", command=lambda: input_key("+")).pack()
Button(window, text="-", command=lambda: input_key("-")).pack()

window.mainloop()