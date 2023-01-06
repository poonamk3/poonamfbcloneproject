import requests,json
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse

# @cache_page(60 * 15)
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user:
            payload=[]
            response = self.get_response(request)
            # print(request.user)
            
            resp=requests.get("http://127.0.0.1:8000/api/post/")
            # resp_dict = json.loads(resp.text)
            # print(resp_dict)
            data=resp.text
            # print(data)
            db=None
            if cache.get("key"):
                data= cache.get("key")
                db='redis'
            else:
                cache.set("key",data,timeout=22)
                db='postgres'
            # print({'data':data,'db':db})


        else:
            print("fail")
        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_view(request,*args,**kwargs):
    #     resp=requests.get("http://127.0.0.1:8000/api/post/")
    #     data=resp.text
    #     return HttpResponse(data)