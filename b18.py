# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:28:51 2024

@author: Chi
"""
##Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:

#- Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
#- Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các từ).
def question_18(s:str):
    chuoi = s.split()
    chuoihoanhao = " ".join(chuoi)
    return chuoihoanhao
print(question_18("   Hello    world!   "))