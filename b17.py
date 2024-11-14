# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:53:54 2024

@author: Chi
"""
##Viết một hàm để tạo ra một danh sách gồm `n` số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, sắp xếp danh sách theo thứ tự giảm dần.
import random
def question_17(n: int):
    m = [random.randint(1,100) for _ in range(n)]
    m.sort(reverse=True)
    return m
print(question_17(5))
