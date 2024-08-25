# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang - 23709171"
import random
luachon=["kéo", "búa", "bao"]

nguoichoi = input("Người chơi chọn: ")
nguoimay = random.choice(luachon)

print("Máy tính chọn:", nguoimay)
if nguoichoi == nguoimay:
    print("Kết quả: Hòa")
elif nguoichoi == "kéo" and nguoimay == "bao":
    print("Kết quả: Người chơi thắng")
elif nguoichoi == "búa" and nguoimay == "kéo":
    print("Kết quả: Người chơi thắng")
elif nguoichoi == "bao" and nguoimay == "búa":
    print("Kết quả: Người chơi thắng")
else:
    print("Kết quả: Người chơi thua")