import pytest


@pytest.fixture
def setup():
	print("This is run first")
	yield 
	print("This is run End")

def test(setup):
	assert 3 == 3
	print(" 3 equal 3")

