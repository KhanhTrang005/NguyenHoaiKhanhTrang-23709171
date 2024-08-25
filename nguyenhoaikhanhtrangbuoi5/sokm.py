# -*- coding: utf-8 -*-


"""


@author:Nguyễn Hoài Khánh Trang 23709171
"""

sokm= float(input("Nhập số km mình đi được: "))
Tongtien = 0 
if sokm == 1 :
    Tongtien = sokm*20
elif 1 < sokm <= 3 :
    Tongtien = sokm*13
elif 4 <= sokm <= 8 :
    Tongtien = 3*13 + (sokm-3)*12
else:
    Tongtien = 3*13 + (sokm - 3)*12 + (sokm-8)*10

if Tongtien >100:
    Tongtien = (3*13 + (sokm - 3)*12 + (sokm-8)*10) * 0.92
print("Tổng số tiền phải trả cho taxi: ", int(Tongtien), "VND")
