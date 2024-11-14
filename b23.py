# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:17:32 2024

@author: Chi
"""

#23 Kiểm tra giá trị trùng lặp trong mảng
from typing import List
def question_23(nums: List[int]):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
print(question_23(nums = [1,2,3,1]))