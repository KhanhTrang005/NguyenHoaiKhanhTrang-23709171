# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:08:21 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

so = int(input("Nhập 4 số xe: "))

nguyen1 = so // 1000
du1 = so %1000

nguyen2 = du1 // 100
du2 = du1 % 100

nguyen3= du2 // 10
du3 = du2 % 10

nguyen4 = du3 
tinh = nguyen1 + nguyen2 + nguyen3 + nguyen4
cuoi = tinh %10 + tinh//10

print("Số nút 4 chữ số = ",cuoi)
