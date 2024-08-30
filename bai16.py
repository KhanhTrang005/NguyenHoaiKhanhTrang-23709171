# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:48:07 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""
h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))

if h < 0 or m >=60 or s >= 60:
    print("Thời gian không hợp lệ, vui lòng nhập lại")
else: 
    tong = h*3600 + m*60 +s
    print("Tính {}h{}p{}s = {} giây".format(h,m,s,tong))
   