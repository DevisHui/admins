# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:53:18 2024

@author: Chi
"""

#25 Sắp xếp các bình phương của một mảng đã sắp xếp
from typing import List
def question_25(nums: List[int]):
    binhphuong=[]
    for i in nums:
        binhphuong.append(i**2)
        binhphuong.sort()
    return binhphuong
print(question_25( nums = [-4, -1, 0, 3, 10]))