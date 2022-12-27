# Pytest - Xfail/Skip Tests
import pytest

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200