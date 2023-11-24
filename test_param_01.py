#!/usr/bin/env python


import pytest


"""
Parametrization enables one to perform multiple calls to the same test 
function. The developer can define a set of arguments, so each call to the 
test function gets its own set of arguments
"""


def add_some_numbers(a: int, b: int) -> int:
    return a + b


@pytest.mark.parametrize("a, b, exp_res", [(5, 5, 10), (2, -5, -3)])
def test_add_some_numbers(a, b, exp_res):
    assert add_some_numbers(a=a, b=b) == exp_res