# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:52:00 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))
d = int(input("Nhập số thứ 4: "))

so_nho = a
if b < so_nho :
    so_nho = b
if c < so_nho:
    so_nho = c
if d < so_nho:
    so_nho = d
    
print("Số nhỏ nhất: ", so_nho)

