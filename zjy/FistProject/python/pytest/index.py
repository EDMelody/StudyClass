#
''''''

"""
  qew
"""

import pytest

def func(x):
    return x + 1
def test_answer():
    assert func(4) == 5

# test_answer()
def f():
    raise SystemExit(1)
def test_mytest():
  with pytest.raises(SystemExit):
      f()