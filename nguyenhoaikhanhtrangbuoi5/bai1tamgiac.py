# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang - 23709171"
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, và c là ba cạnh của một tam giác.")
else:
    print("a, b, và c không phải là ba cạnh của một tam giác.")