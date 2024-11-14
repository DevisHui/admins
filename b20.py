# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:06:14 2024

@author: Chi
"""
#Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về `None`.
def question_20():
    a = input("Nguoi dung nhap: ")
    if a == "":
        return None
    return a
print(question_20())