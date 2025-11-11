# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 14:57:31 2025

@author: huangjiaqi
"""

# 用户输入字符串
s = input("请输入一个字符串：")

# 转换为小写，忽略大小写
s_lower = s.lower()

# 判断是否为回文
if s_lower == s_lower[::-1]:  # 字符串切片[::-1]表示倒序
    print(f"字符串 '{s}' 是回文")
else:
    print(f"字符串 '{s}' 不是回文")