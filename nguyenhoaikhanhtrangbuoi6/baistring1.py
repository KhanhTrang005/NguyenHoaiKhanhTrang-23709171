# -*- coding: utf-8 -*-
" Nguyễn Hoài Khánh Trang - 23709171 "

hien_thi = "Đại học Quốc Gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
#bài 1
for i in hien_thi.split(', '):
    print(i)
#bài 2
n = (hien_thi.replace('P.','').replace('Q.','').replace('Tp.','') .split(', ')) 
for hien_thi in n:
    print(hien_thi)
