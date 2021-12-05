# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:28:22 2021

@author: Kichiro
"""
from tkinter import *

top = Tk()
def callback():
    print(Entry2.get())
    print(Entry1.get())
    top.destroy()

top.title('log in')
L1 = Label(top, text=" Nama user")
L1.grid(row=0, column=0)
Entry2 = Entry(top,bd= 2)
Entry2.grid(row=0, column=1)

L1 = Label(top, text="Sandi")
L1.grid(row=1, column=0)
Entry1 = Entry(top, bd = 2, show='*')
Entry1.grid(row=1, column=1)
Button1 = Button(top, text="Masuk", width=10, command=callback)

Button1.grid(row=3, column=1)

top.mainloop()