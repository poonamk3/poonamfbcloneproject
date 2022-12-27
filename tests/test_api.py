"""import pytest,requests,json
# from text_dictdata import *
from test_exdata import *


login=login()
register=register()


@pytest.mark.parametrize("number",[register,login])
def test_foo(number):
	if 'first_name' in number:
   		resp=requests.post("http://127.0.0.1:8000/api/registerallapi/",number) 
	assert resp.json()['email'] == "poonamk@gmail.com"

	elif 'email' in number:
		resp=requests.post("http://127.0.0.1:8000/api/loginapi/",number) 
   		print("save")
   		print(resp)
   	assert resp.json()['email'] == "admin@gmail.com"
"""

"""
@pytest.mark.parametrize("number",[login])
def test_foo(number):
	import pdb;pdb.set_trace()
	if 'email' in number:
   		resp=requests.post("http://127.0.0.1:8000/api/loginapi/",number) 
   		print("save")
   		print(resp)
	# assert resp.json()['email'] == "admin@gmail.com"
"""

      

