import os

import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open('./datas.yml') as f:
        datas = yaml.safe_load(f)
        add_data = datas["add_datas"]
        sub_data = datas["sub_datas"]
        mul_data = datas["mul_datas"]
        div_data = datas["div_datas"]
        return [add_data, sub_data, mul_data, div_data]


class TestCalc:

    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
