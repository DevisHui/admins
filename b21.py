# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:33:20 2024

@author: Chi
"""

#21 Tìm hai số trong danh sách có tổng bằng một số nguyên cho trước
from typing import Optional, Tuple, List
def question_21(nums: List[int], target: int): 
    ds = {}
    for a in nums:
        socantim = target - a
        if socantim in ds:
            return(socantim, a)
        ds[a] = True
    return None
print(question_21(nums = [2,7,11,15], target = 9))