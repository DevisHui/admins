# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:59:28 2024

@author: Chi
"""

#16 Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị trung bình cộng của chúng
def question_16(*arg):
    if len(arg) == 0:
        return None
    tong= sum(arg)
    dem= len(arg)
    return tong/dem
print(question_16(1,2,3,4,5))
