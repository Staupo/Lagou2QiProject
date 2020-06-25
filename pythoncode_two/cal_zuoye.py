# -*- coding: utf-8 -*-
# @Time   : 2020-06-25 12:19
# @Author : Saber
# @File   : cal_zuoye.py

class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print('被除数不能为0')
        else:
            return a / b
