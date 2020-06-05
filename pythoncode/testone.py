# -*- coding: utf-8 -*-
# @Time   : 2020-06-03 22:36
# @Author : Saber
# @File   : testone.py

# 函数式编程：无return返回值，返回None
def func_one():
    print(5 + 6)
result_1 = func_one()


# 面向过程：有return返回值的情况，返回表达式的值
def func_two():
    return 7 + 8
result_2 = func_two()


# 有参数的时候若没有给默认值，调用时必须传递参数才能调用
def func_three(saber):
    print(saber)


# 有参数的时候若给了默认值，调用时可不传递参数，返回默认值
def func_four(name='chengchen', girlfriend='没有女朋友'):
    print(name + "没有女朋友")


if __name__ == '__main__':
    print(result_1)
    print(result_2)
    func_three('chencghen')
    func_four()
