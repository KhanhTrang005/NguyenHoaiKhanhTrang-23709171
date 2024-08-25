# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang - 23709171"
thoigian = input("Thời gian nhập vào: ")

hh, mm, ss = map(int, thoigian.split(":"))

print("Tổng số giây thời gian: ", hh*3600+ mm*60 +ss)