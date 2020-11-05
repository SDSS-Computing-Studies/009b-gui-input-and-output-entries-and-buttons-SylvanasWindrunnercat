"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk
import math

window = tk.Tk()
window.title("Calculater")
window.geometry("400x400")

eoutput = StringVar()
eoutput.set("Output goes here")

def tri():
    b = e1.get()
    b = float(b)
    c = e2.get()
    c = float(c)
    d = (b**2) - (4*c)
    sol1 = (-b - math.sqrt(d)) / 2
    sol2 = (-b + math.sqrt(d)) / 2

    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = tk.Label(window,text = "Please enter the value of 'b' and 'c'")
l2 = tk.Label(window,text = "to decompose this trinomial")
l3 = tk.Label(window,text = "value of b is:")
l4 = tk.Label(window,text = "value of c is:")
l5 = tk.Label(window,text = "The output is")
e1 = tk.Entry(window,width = 10)
e2 = tk.Entry(window,width = 10)
l6 = tk.Label(window,text = sol1,sol2)
b1 = tk.Botton(window,text = "Calculate",command = tri)

l1.grid(row = 1,column = 1)
l2.grid(row = 2,column = 1)
l3.grid(row = 3,column = 1)
l4.grid(row = 3,column = 3)
e1.grid(row = 3,column = 2)
e2.grid(row = 3,column = 4)
l6.grid(row = 4,column = 2)
b1.grid(row = 4,column = 1)

win.mainloop()
