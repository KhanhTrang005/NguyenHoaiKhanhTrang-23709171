# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:41:14 2024

@author: Nguyễn Hoài Khánh Tràng - 23709171
"""
hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))


if hh < 0 or mm >=60 or ss >= 60:
    print("Thời gian nhập không hợp lệ vui lòng nhập lại")
else:
    print("Thời gian nhập vào: {}:{}:{} ".format(hh,mm,ss))
    print("Tổng số giây thời gian: ", hh*3600+ mm*60 +ss)