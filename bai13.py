# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"Nguyễn Hoài Khánh Trang - 23709171"
dd = int(input("Ngày: "))
mm = int(input("Tháng: "))
yy = int(input("Năm: "))
print("Nhập ngày tháng năm: {} {} {} ".format(dd,mm,yy))

#a
print("Ngày/tháng/năm: {}/{}/{} ".format(dd,mm,yy))
#b
print("Ngày/tháng/năm: {}/{}/{:02d} ".format(dd,mm,yy % 100 ))
#c
print("Năm/tháng/ngày: {}/{}/{} ".format(yy,mm,dd))
