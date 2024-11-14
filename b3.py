# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:00:36 2024

@author: Chi
"""

#Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết thường trong chuỗi đó
def question_3(s:str):
    hoa=0
    thuong=0
    for i in s:
        if i.isupper():
            hoa+=1
        if i.islower():
            thuong+=1
    return hoa,thuong
print(question_3("Nguyễn Hồng Huy"))