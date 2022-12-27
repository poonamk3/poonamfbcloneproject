"""
import pytest,requests,json


@pytest.fixture
def fixture_1():
   user_data={
      "username":"dipeshpatidar",
      "first_name":"poonam",
      "last_name":"sfd",
      "email":"poonamkumar@gmail.com",
      "password":"asdf@123"
   }
   return user_data

def test_api_post(fixture_1):
   resp=requests.post("http://127.0.0.1:8000/api/registerallapi/",fixture_1)
   print(resp.json())
   print(resp)
   assert resp.json()['email'] == "poonamkumar@gmail.com"

   
"""