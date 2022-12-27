import pytest,requests,json
from text_ex13 import *
import logging
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

data=valuedata()
datas=valuedata2()

@pytest.mark.parametrize("number",[data,datas])
def test_foo(number):
   mylogger.info('Function Testing')
   for i in range(len(number)):
      assert number["to"]== "2799900001" 


# if __name__ == '__main__':
#     mylogger.info(' About to start the tests ')
#     pytest.main(args=[os.path.abspath(__file__)])
#     mylogger.info(' Done executing the tests ')