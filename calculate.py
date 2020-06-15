# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:29:54 2020

@author: sadik
"""
print("ilk sayiyi giriniz")
x=int(input())
print("ikinci sayiyi giriniz")
y=int(input())
print("toplama icin 1 cikartma icin 2 carpma icin 3 u bolme icin 4 u seciniz")
z=int(input())
def toplama(x,y):
    print(x+y)
def cikarma(x,y):
    print(x-y)
def carpma(x,y):
    print(x*y)
def bolme(x,y):
    print(x/y)

if z==1:
    toplama(x,y)
if z==2:
    cikarma(x,y)
if z==3:
    carpma(x,y)
if z==4:
    bolme(x,y)
