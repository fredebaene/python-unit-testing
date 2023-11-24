#!/usr/bin/env python


def add_two(x: int) -> int:
    return x + 2


def test_add_two():
    assert add_two(4) == 6