# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:34:30 2024

@author: Nguyễn Hoài Khánh Trang - 237709171
"""

can_nang= float(input("Nhập cân nặng (kg): "))
chieu_cao= float(input("Nhập chiều cao (m): "))

BMI =  can_nang/(chieu_cao**2)

print("Kiểm tra sức khỏe BMI: ", round(BMI,1))

