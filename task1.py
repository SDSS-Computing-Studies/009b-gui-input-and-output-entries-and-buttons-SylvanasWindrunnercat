"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("400x400")

a = ""
b = ""
c = ""
d = ""

def blank1():
    a = e1.get()
    a = float(a)
    if a == 11042020:
        b = 11.04.2020
    elif a == "name":
        b = "NAME"
    elif a == "adjective":
        c = "ADJECTIVE"
    elif a == "noun":
        d = "NOUN"
    a_entry.delete(0,END)
    a_entry.insert(0,answer)

e1 = tk.Entry(window,width = 20)
l1 = tk.Label(window,text = "DATE:")
l2 = tk.Label(window,text = "Please excuse")
l3 = tk.Label(window,text = b)
l4 = tk.Label(window,text = "who is far too")
l5 = tk.Label(window,text = "to attend")
l6 = tk.Label(window,text = c)
l7 = tk.Label(window,text = "class.")
l8 = tk.Label(window,text = d)
b1 = tk.Botton(window,text = "fill")

e1.grid(row = 1,column = 1)
l1.grid(row = 2,column = 1)
l2.grid(row = 3,column = 1)
l3.grid(row = 4,column = 1)
l4.grid(row = 5,column = 1)
l5.grid(row = 6,column = 1)
l6.grid(row = 5,column = 2)
l7.grid(row = 6,column = 3)
l8.grid(row = 6,column = 2)
b1.grid(row = 1,column = 2)

win.mainloop()
