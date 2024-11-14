# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:19:03 2024

@author: Chi
"""

#26 Tìm độ dài của chuỗi palindrome dài nhất có thể được tạo ra
from collections import Counter
def question_26(s: str)-> int:
    demchuoi = Counter(s)
    dodai = 0
    cokitule = False
    for dem in demchuoi.values():
        dodai += dem // 2*2
        if dem % 2 ==1:
            cokitule = True
    if cokitule:
        dodai +=1
    return dodai
print(question_26("abccccdd"))
