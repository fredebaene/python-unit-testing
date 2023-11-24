#!/usr/bin/env python


"""
When running pytest, pytest looks for test files in the current working 
directory and its subdirectories. These test files have file names that follow 
one of the following two patterns: `test_*.py` or `*_test.py`.

There are multiple ways to select what tests you want to run:

1) to run all tests in the current working directory and subdirectories:

```
pytest
```

2) to run all tests contained in a specific subdirectory, e.g., `testing`:

```
pytest testing
```

3) to run all tests defined in a specific test file:

```
pytest test_example_01.py
```

4) to run all tests defined in a couple of specific test files:

```
pytest test_example_01.py test_example_02.py
```

5) to run a specific test in a specific test file:

```
pytest test_example_01.py::test_add_one
```

6) to run a specific test defined inside a specific test class:

```
pytest test_class.py::TestClass::test_two
```

7) to run tests with specific markers

```
pytest -m slow
```

This will run all tests with the marker `@pytest.mark.slow`.

There are two ways of invoking pytest. You can invoke pytest directly using 
the command `pytest [...]` on the command line. Or you can invoke it using the 
command `python -m pytest [...]`. The second option will add the current 
directory to `sys.path`.
"""


def add_one(x: int) -> int:
    return x + 1


def test_add_one():
    assert add_one(5) == 6