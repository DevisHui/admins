# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:13:58 2024

@author: Chi
"""

#6 Tính giai thừa của một số nguyên dương
def question_6(n: int):
    giaithua=1
    for i in range(1,n+1):
        giaithua *=i
    return giaithua
print(question_6(5))