# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:44:11 2021

@author: Kichiro
"""

import random
import string

print('halo, selamat datang ke Generator Password')

#memasukkan panjang dari Password
length = int(input('\n masukkan panjang dari password yang diinginkan : '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation 

#menggabungkan data
all = lower + upper + num + symbols

#menggunakan Library random
temp = random.sample(all,length)

#membuat password
password = "".join(temp)

#menampilkan password
print(password)