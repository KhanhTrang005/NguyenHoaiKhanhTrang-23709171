# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:50:54 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""
h1 = int(input("Nhập giờ 1: "))
m1 = int(input("Nhập phút 1: "))
s1 = int(input("Nhập giây 1: "))

h2 = int(input("\nNhập giờ 2: "))
m2 = int(input("Nhập phút 2: "))
s2 = int(input("Nhập giây 2: "))

if h1 < 0 or h2 < 0 or m1 >= 60 or m2 >=60 or s1 >= 60 or s2 >=60:
    print("Thời gian không hợp lệ, vui lòng nhập lại")
else:
    tong_s1 = h1*3600 + m1*60 + s1
    tong_s2 = h2*3600 + m2*60 + s2 
    tong_giay = tong_s1 + tong_s2
    
    if tong_s2 > tong_s1:
        hieu_giay = tong_s2 - tong_s1
    else: 
        hieu_giay = tong_s1 - tong_s2

    gio1 = tong_giay // 3600
    phut1 = (tong_giay % 3600) // 60 
    giay1 = (tong_giay % 3600) % 60
    
    gio2 = hieu_giay // 3600
    phut2 = (hieu_giay % 3600) // 60 
    giay2 = (hieu_giay % 3600) % 60
    
    print("Tổng 2 giờ = {} giờ {} phút {} giây ".format(gio1,phut1,giay1))
    print("Hiệu 2 giờ = {} giờ {} phút {} giây".format(gio2,phut2,giay2))