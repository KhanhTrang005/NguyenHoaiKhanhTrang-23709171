# -*- coding: utf-8 -*-
"Nguyễn Hoài Khánh Trang - 23709171"

print("============ MENU ============")
print("\t1. Hu tieu ")
print("\t2. Chao long")
print("\t3. Banh canh")
print("\t4. Bun rieu")
print("\t5. Pho bo")
print("==============================")
lua_chon =  int(input("Moi nhap lua chon: "))
if lua_chon == 1:
    print("\tHu tieu")
elif lua_chon == 2:
    print("\tChao long")
elif lua_chon == 3:
    print("\tBanh canh")
elif lua_chon == 4:
    print("\tBun rieu")
elif lua_chon == 5:
    print("\tPho bo")
else:
    print("Món bạn chọn không có menu, vui lòng nhập từ 1-5")
print("==============================")