"""import pytest,requests,json
data={
   "username":"dipesh",
   "first_name":"dipesh",
   "last_name":"patidar",
   "email":"dipesh@gmail.com",
   "password":"asdf@123"
}


def test_api_get():
   resp=requests.get("http://127.0.0.1:8000/api/registerallapi/")
   print(resp)
   print(resp.json())
   print(resp.url)


def test_api_post():
   resp=requests.post("http://127.0.0.1:8000/api/registerallapi/",data)
   print(resp.json())
   assert resp.json()['email'] == "dipesh@gmail.com"



# def test_api_delete():
#     resp=requests.delete("http://127.0.0.1:8000/api/registerallapi/6/")
#     print(resp.status_code)
#     assert resp.status_code == 404



data={
   "id": 4,
   "username":"d",
   "first_name":"dipesh",
   "email":"dipesh@gmail.com"
}
def test_api_post():
   resp=requests.patch("http://127.0.0.1:8000/api/registerallapi/4/",data)
   print(resp.json())
   assert resp.json()['email'] == "dipesh@gmail.com"
"""