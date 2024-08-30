# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:05:00 2024

@author:Nguyễn Hoài Khánh Trang - 237709171
"""

a = input("Nhập 1 kí tự là chữ thường: ")

if a.islower() and len(a) == 1 :
    print("Kí tự chữ hoa tương ứng: ", a.upper())
else:
    print("Vui lòng nhập chữ thường, chỉ 1 kí tự ")