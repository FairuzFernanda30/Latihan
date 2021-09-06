# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:34:41 2021

@author: Kichiro
"""

apple_price = 2
money = 20

input_count = input('mau berapa apel ? :')
count=int(input_count)
total_price= apple_price*count

print('anda akan membeli ' + str(count) + ' apel')
print('harga total adalah ' + str(total_price) + ' dolar')

if money > total_price:
    print('anda telah membeli ' + str(count) + ' apel')
    print('uang anda tinggal ' + str(money-total_price) + ' dolar')

elif money == total_price:
    print('anda telah membeli ' + str(count)+ ' apel ')
    print(' dompet anda kosong ')

else:
    print(' uang anda tidak mencukupi ')
    print(' anda akan menghutang ke reternir 2')