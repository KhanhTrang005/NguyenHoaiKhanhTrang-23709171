# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:22:59 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))

if 0 <= gio <= 2 and 0<= phut <= 59 and 0 <= giay <= 59:
    print("Thời gian hợp lệ")
else:
    if gio < 1 or gio > 24:
        print("Giờ không hợp lệ")
    if phut < 0 or phut > 59:
        print("Phút không hợp lệ")
    if giay <0 or giay >59:
        print("Giây không hợp lệ")