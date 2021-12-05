# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:12:49 2021

@author: Kichiro
"""

from tkinter import *

root = Tk()

label_1 = Label(root, text="Nama")
label_2 = Label(root, text="Sandi")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="keep me log in")
c.grid(columnspan=2)
root.mainloop()