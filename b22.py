# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:50:39 2024

@author: Chi
"""

#22 Di chuyển tất cả các số 0 về cuối mảng
from typing import List
def question_22(nums: List[int]):
    so= 0
    for i in range(len(nums)):
       if nums[i] !=0:
           nums[so], nums[i]= nums[i], nums[so]
           so+=1
    return nums   
print(question_22(nums = [0,1,0,3,12]))