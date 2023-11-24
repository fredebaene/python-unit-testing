#!/usr/bin/env python


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        a = 4
        assert (a - 1) == 3