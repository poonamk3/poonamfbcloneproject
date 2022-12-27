from functools import wraps
import pytest     
import logging
import time 
from timeit import default_timer as timer
from utils import *


# logging.basicConfig(level=logging.DEBUG)
# mylogger = logging.getLogger()                                                                                                                                                                             



logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
"""def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper
"""
@timeit
def test():
    # mylogger.info('Function Testing')
    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warning("Its a Warning")
    logger.error("Did you try to divide by zero")
    logger.critical("Internet is down")
    assert 3 == 3
    print(" 3 equal 3")
test()

