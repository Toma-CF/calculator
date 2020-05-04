#!/usr/bin/env python3

from tkinter import *
window = Tk()

# bufferExpression = [] 
bufferString = ""

def equal():
	global bufferString
	values = bufferString.split("+")
		
	rslt = 0;

	for value in values: 
		rslt += int(value)

	bufferString = ""
	print (rslt)
	#"45+76"
	# ['45', '76']

def digit(value):
	global bufferString
	bufferString += value
	print("Buffersting: " + bufferString)

def input_key(param):
	digit(param)

Button(window, text="0", command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text="1", command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text="2", command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text="3", command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text="4", command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text="5", command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text="6", command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text="7", command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text="8", command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text="9", command=lambda: input_key("9")).grid(row=3, column=2)
Button(window, text="+", command=lambda: input_key("+")).grid(row=3, column=3)
Button(window, text="=", command=lambda: equal()).grid(row=5, column=3)
Button(window, text="Close", command=window.quit).grid(row=0, column=3)

window.mainloop()