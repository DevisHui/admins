# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:35:30 2024

@author: Chi
"""

#7  Tạo danh sách n số thực ngẫu nhiên và tìm số lớn nhất, nhỏ nhất
import random
def question_7 (n: int):
    thucngau = [random.uniform(0, 1) for _ in range(n)]
    solon = max(thucngau)
    sonho = min(thucngau)
    return solon, sonho
print(question_7(2))