# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:32:38 2024

@author: Nguyễn Hoài Khánh Trang - 23709171
"""

N = int(input("Nhập 2 số N nguyên dương = "))

if 9 < N < 100:
    tong2so = (N//10) + (N%10)
    print ("Tổng 2 số trong N = ", tong2so)
else:
    print("Bạn phải nhập 2 số, vui lòng nhập lại ")