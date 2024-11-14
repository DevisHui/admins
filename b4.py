# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:08:00 2024

@author: Chi
"""

#Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không. Trả về `True` nếu số đó là số chẵn, và `False` nếu là số lẻ.

def question_4(n: int):
    if n%2==0:
        return True
    else:
        return False
print(question_4(4))
print(question_4(23))        