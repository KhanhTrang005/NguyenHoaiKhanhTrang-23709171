# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:31:25 2024

@author: Nguyễn Hoài Khánh Trang-23709171
"""

a= int(input("Nhập a = "))
b = int(input("Nhập b = "))

tong = a+b
hieu = a-b
tich = a*b
thuong = a/b

print ('Tổng: {} + {} = {} '.format(a,b,tong))
print ('Hiệu: {} - {} = {} '.format(a,b,hieu))
print ('Tích: {} x {} = {} '.format(a,b,tich))
print ('Thương: {} : {} = {} '.format(a,b,round(thuong,3)))