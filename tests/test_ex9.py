"""import pytest
value=[1, 2, 3, 0, 42]
@pytest.mark.parametrize("number", value)
def test_foo(number):
    assert number >= 0 
"""

"""import pytest

@pytest.fixture
def input_value():
   input = 36
   return input
@pytest.mark.parametrize("number", input_value)
def test_divisible_by_3(number):
   assert number % 3 == 0

def test_divisible_by_6(input_value):
   assert number % 6 == 0
"""


import pytest
value=[10,1,3]
value1=[10,5]
@pytest.mark.parametrize("number", [value,value1])
def test_foo(number):
	for i in range(len(number)):
		assert number[0] >= 10 


