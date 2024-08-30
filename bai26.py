# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:17:02 2024

@author:Nguyễn Hoài Khánh Trang - 237709171
"""
#1
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))
c = int(input("Nhập c = "))

if a > b:
    a,b = b,a 
if a > c:
    a,c = c,a 
if b > c:
    b,c = c,b
    
print("Xếp theo thứ tự: ",a,b,c )

