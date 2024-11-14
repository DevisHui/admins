# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:07:43 2024

@author: Chi
"""

#24 Tìm phần tử chiếm đa số trong mảng
from typing import List
def question_24(nums: List[int]):
    phantu = None
    dem = 0
    for so in nums:
        if dem == 0:
            phantu = so
        dem+=1 if so == phantu else -1
    return phantu
print(question_24(nums = [3,2,3]))