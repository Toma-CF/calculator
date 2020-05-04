#!/usr/bin/env python3

from tkinter import *
window = Tk()

def hello():
	print("hello")
	pass

Button(window, text="Add smth", command=window.quit).pack()
Button(window, text="hello", command=hello).pack()
Button(window, text="Close", command=window.quit).pack()
window.mainloop()