# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:56:07 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

hinh = input("Nhập hình: ")
v = "hình vuông"
n = "hình chữ nhật"
t = "hình tròn"

if hinh == v:
    canh = int(input("Nhập cạnh của hình vuông = "))
    print("P = ", canh*4)
    print("S = ", canh*canh)
elif hinh == n:
    rong = int(input("Nhập chiều rộng = "))
    dai = int(input("Nhập chiều dài = "))
    print("P = ", (dai+rong)*2)
    print("S = ", dai*rong)
elif hinh == t:
    r = int(input("Nhập bán kính = "))
    print("P = ", r*2*3.14)
    print("S = ", (r**2)*3.14)