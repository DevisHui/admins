# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:03:37 2024

@author: Chi
"""


#11 Viết một hàm `question_11(n)` để trả về số Fibonacci thứ `n`. Dãy số Fibonacci được định nghĩa như sau:
import random
def question_11(n:int):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else: 
        return question_11(n-1) + question_11(n-2)
print(question_11(5))