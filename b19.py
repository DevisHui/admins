# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:04:44 2024

@author: Chi
"""

#19  Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên cho trước n hay không.
def question_19(x: int, n:int):
    if x>n:
        return True
    return False
print(question_19(15, 10))