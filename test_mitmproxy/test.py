# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-20  下午2:33
# @Author  : 张晨旭
# @IDE     : PyCharm
# @File    : test.py
# from jsonpath import jsonpath
# a = {"nsme": {"age":[1,3,3]}}
# x = jsonpath(a, "$..age")
# print(x)
# x[0][1] = 4
# print(x)

import hashlib         #导入hashlib模块

md = hashlib.md5()     #获取一个md5加密算法对象
md.update('how to use md5 in hashlib?'.encode('utf-8'))                   #制定需要加密的字符串
print(md.hexdigest())  #获取加密后的16进制字符串
