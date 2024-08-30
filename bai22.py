# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang 23709171"

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm ")
    else:
        print("Phương trình vô nghiệm ")
else:
    x = -b/a
    print("Phương trình có nghiệm là :",float(x))