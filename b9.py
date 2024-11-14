# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:12:05 2024

@author: Chi
"""

#9 Viết một hàm để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không.
def question_9(s: str):
    s = ''.join(char for char in s if char.isalnum())
    s = s.lower()
    return s == s[::-1]
print(question_9("race a car"))