# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:35:04 2024

@author: Chi
"""

#10 Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống.
def question_10(so):
    if so is None:
        nhapchuoi= input= ("Nhập các số nguyên (cách nhau bởi khoảng trắng")
        so= nhapchuoi.split()
        so= [int(num) for num in so]
    if so:
        return so
    else:
        return None
 

    
if __name__ == "__main__":
    print(question_10([1,2,3]))
    print(question_10([]))