import pytest , math
"""def test_greater():
   num = 100
   assert num > 100"""

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200



@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5