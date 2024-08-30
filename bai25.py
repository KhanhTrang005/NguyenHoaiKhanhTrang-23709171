# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:30:48 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

chu = input("Nhập 1 chữ cái: ")

if len(chu) == 1:  
    if chu.islower():
        print("Đổi thành: ", chu.upper()) #hàm upper dùng đổi từ chữ thường sang in hoa
    else:
        print("Đổi thành: ", chu.lower()) #hàm lower dùng đổi từ in hoa sang chữ thường
else:
    print("Vui lòng nhập lại chỉ 1 chữ cái")
