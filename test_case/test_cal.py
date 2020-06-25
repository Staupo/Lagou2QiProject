# -*- coding: utf-8 -*-
# @Time   : 2020-06-25 12:48
# @Author : Saber
# @File   : test_cal.py


import pytest
import yaml


@pytest.mark.parametrize('saber', yaml.safe_load(open('./saber.yaml')))
class TestCal:

    def test_add(self, larry, saber):
        a = saber["add"]["a"]
        b = saber["add"]["b"]
        assert a + b == larry.add(a, b)

    def test_minus(self, larry, saber):
        a = saber["add"]["a"]
        b = saber["add"]["b"]
        assert a - b == larry.minus(a, b)

    def test_multiply(self, larry, saber):
        a = saber["add"]["a"]
        b = saber["add"]["b"]
        assert a * b == larry.multiply(a, b)

    def test_div(self, larry, saber):
        a = saber["add"]["a"]
        b = saber["add"]["b"]
        assert a / b == larry.div(a, b)
