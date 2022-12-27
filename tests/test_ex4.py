import pytest




@pytest.fixture
def setup():
   print("This is run first Dictionary ")
   yield 
   print("This is run End Dictionary ")

def test(setup):
   assert 2+3 == 5
   assert 3+3 == 6
   print(" a,b equal final")  

def test_program():
   a=4
   b=5
   assert a+2 == 6 ,"Addition do not match"
   print("save")

@pytest.mark.parametrize("a,b",[(3+5,8),(2+4,6),(8+9,17)])
def test_eval(a,b):
    assert a == b


@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output


@pytest.fixture
def function_fixture():
   print('Fixture for each test')
   return 1

def test_programs():
   a=4
   b=5
   assert a+2 == 6 ,"Addition do not match"
   print("save")


@pytest.fixture(scope='module')
def module_fixture():
   print('Fixture for module')
   return 2



