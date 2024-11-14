# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:24:11 2024

@author: Chi
"""
#13  Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự không phải khoảng trắng
def question_13(s: str):
    tu = s.split()
    return len(tu)
print(question_13(" vãi cứt anh huy đẹp zai"))
