# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang 23709171"

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a + b > c) or (a + c > b) or (b + c > a):
    print("Đây là tam giác thường")
    if   a == b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Đây là tam giác vuông")

else:
    print("a, b, và c không phải là ba cạnh của một tam giác ")