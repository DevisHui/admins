# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:08:27 2024

@author: Chi
"""

#12  Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số đó có phải là số nguyên tố hay không.
import random
def question_12(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True 
n= random.randint(1, 1000)
print(question_12(37))