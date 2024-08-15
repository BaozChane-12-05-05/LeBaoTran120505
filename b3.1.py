# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:24:09 2024

@author: pc5
"""

print("Chương trình tính điểm trung bình của các học sinh ")
GPA = float(input("Nhập điểm trung bình"))
if GPA < 3.5:
    print("Học lực Kém")
elif GPA >= 3.5 and GPA <= 5.0:
    print("Học lực Yếu")
elif GPA >= 5.0 and GPA <= 7.0:
    print("Học lực Trung Bình")
elif GPA >= 7.0 and GPA <= 8.0:
    print("Học lực Khá")
elif GPA >= 8.0 and GPA <= 9.0:
    print("Học Lực Giỏi")
elif GPA >= 9.0 and GPA <= 10.0:
    print("Học lực Xuất sắc")
else:
    print("Không xác định")