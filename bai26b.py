# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:05:00 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""
#26b
N = input("Nhập vào dãy số nguyên N: ")

a, b, c, d = int(N[0]), int(N[1]), int(N[2]), int(N[3])

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if a > d:
    a,d = d,a
if b > c:
    b,c = c,b
if b > d:
    b,d = d,b
if c > d:
    c,d = d,c    
    
print("Số tăng dần: {}{}{}{}".format(a,b,c,d))