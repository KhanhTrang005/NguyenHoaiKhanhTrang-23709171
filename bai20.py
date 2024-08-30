# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:54:57 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""
a  = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

so_lon = a 
if so_lon < b:
    so_lon = b
if so_lon < c:
    so_lon = c
    
print("Số lớn nhất: ", so_lon)
    