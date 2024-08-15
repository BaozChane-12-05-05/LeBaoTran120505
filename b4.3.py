# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:03:57 2024

@author: pc5
"""

a = float(input("Nhập số km quãng đường"))
sotienla = 0
if a <=1:
    sotienla = 20000
elif a <=3:
    sotienla = (a-1)*13000
elif a <=8:
    sotienla = 3*13000+(a-3)*12000
else:
    sotienla = 3*13000+(a-3)*12000+(a-8)*10000
if sotienla > 100000:
    sotienla = (3*13000+(a-3)*12000+(a-8)*10000) * 0.92
print("tổng tiền là: ", int(sotienla))
    
    