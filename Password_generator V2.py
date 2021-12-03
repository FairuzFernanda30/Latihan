# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:44:11 2021

@author: Kichiro
"""

import random
import string

print('=== halo, selamat datang ke1 Generator Password ===')

#memasukkan panjang dari Password
length = int(input('\n masukkan panjang dari password yang diinginkan : '))

#define data
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
num = list (string.digits)
symbols = list (string.punctuation) 
alphabet = list(string.ascii_letters)
digits = list(string.digits)

#menggabungkan data
all = lower + upper + num + symbols + alphabet + digits

#menggunakan Library random
temp = random.sample(all,length)

#membuat password
password = "".join(temp)

#menampilkan password
print(password)