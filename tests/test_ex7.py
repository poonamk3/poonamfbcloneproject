"""# Register Api Testing
import pytest,requests,json
data={
   "username":"dp",
   "first_name":"dipesh",
   "last_name":"patidar",
   "email":"dipesh@gmail.com",
   "password":"asdf@123"
}
def test_api():
   resp=requests.post("http://127.0.0.1:8000/api/registerallapi/",data)
   print(resp)

def test_get():
   resp=requests.get("http://127.0.0.1:8000/api/registerallapi/")
   json_res=resp.json()
   print(json_res["data"][0]["email"])


   
"""