# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:56:38 2024

@author: Chi
"""
#Viết một hàm để tìm phần tử `x` trong một danh sách `lst`. Nếu tìm thấy, trả về vị trí (chỉ số) của phần tử đó, nếu không, trả về `None`.
def question_5(lst: list, x: int):
    if x in lst:
        return lst.index(x)
    return None
print(question_5(lst = [1,2,3,4,5], x = 3))
print(question_5(lst = [10, 20, 30, 40], x = 25))