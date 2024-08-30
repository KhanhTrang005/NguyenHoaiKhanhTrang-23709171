# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:06:46 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

import math

a = float(input("Nhập a = "))
b = float(input("Nhập b = "))

B1 = (((a+b)/((math.pow(a,1/3) + math.pow(b,1/3)))) - math.pow(a*b,1/3))
B2 =(math.pow(math.pow(a,1/3) - math.pow(b,1/3),2))
chia = B1/B2
print("Kết quả = ",round(chia,3))

