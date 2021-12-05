# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:31:14 2021

@author: Kichiro
"""

from tkinter import *

root = Tk()

def printName(event):
  print("Halo nama saya === UZ")

button_1 = Button(root, text="Print Nama saya")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()