# -*- coding: utf-8 -*-
# @Time   : 2020-06-25 16:49
# @Author : Saber
# @File   : conftest.py


import pytest

from pythoncode_two.cal_zuoye import Calculator


@pytest.fixture(autouse=True)
def larry():
    print('开始计算')
    yield Calculator()
    print('结束计算')
