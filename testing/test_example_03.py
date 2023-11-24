#!/usr/bin/env python


def add_three(x: int) -> int:
    return x + 3


def test_add_three():
    assert add_three(3) == 6