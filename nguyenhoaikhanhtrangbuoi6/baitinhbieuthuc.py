# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang - 23709171"
import math

#1
A = math.pow(32,0.2) - math.pow(1/64, -0.25) + math.pow(8/27,1/3)
print("A = ",float((round(A,3))))
#2
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
phan_so1 = (math.sqrt(a) - math.sqrt(b)) / (math.pow(a,1/4) - math.pow(b, 1/4))
phan_so2 = (math.sqrt(a) + math.pow(a*b,1/4)) / (math.pow(a,1/4) + math.pow(b, 1/4))
B = phan_so1 - phan_so2

if float(round(B,4)) == float(round(math.pow(b,1/4),4)):
    print("Kết quả đúng = ",float(round(B,4)))
else:
    print("Kết quả sai")
    