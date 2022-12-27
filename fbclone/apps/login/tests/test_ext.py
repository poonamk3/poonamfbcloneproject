# Urls test case url=requests.get('home') print(url)


from django.test import SimpleTestCase
from login.views import PostListView,HomeLoginView
from django.urls import resolve,reverse
import requests

from django.contrib.auth.models import User
from django.test import TestCase

class TestUrls(SimpleTestCase):
	def test_list_url_is_resolved(self):
		url = reverse('home')

		# print(resolve(url).func)
		print(resolve(url))
		data=resolve(url).func
		print(data)
		self.assertEquals(data.view_class,PostListView)



import pytest

def test_example():
	assert 1 == 1
	
@pytest.fixture
def fixture_1():
	print("fixture_1")
	return 1

def test_example(fixture_1):
	num=fixture_1
	assert 1 == num
	print("success Testing")


def test_answer():
	a=2
	assert a+3 == 5