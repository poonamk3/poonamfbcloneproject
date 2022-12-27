from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .forms import SignupForm , CommentFrom ,MultiplefieldFrom
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import PostForm,CommentFrom
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from .models import Post,Like,Comment,Multiplefield,Myfrom
from django.views.generic.edit import DeleteView
from bootstrap_modal_forms.generic import BSModalCreateView
from django.shortcuts import  get_object_or_404
from django.urls import reverse_lazy
from login.task import *
from .mailflie import *
from . import signals
from django.core.paginator import Paginator


class IndexView(TemplateView):
    template_name='enroll/home.html'


class HomeView(TemplateView):
    template_name='enroll/homehtml.html'


class RegisterView(CreateView):
    form_class = SignupForm
    template_name='enroll/index.html'
    success_url = '/accounts/login/'
    

@method_decorator(login_required, name='dispatch')  
class PostView(CreateView):
    model= Post
    form_class = PostForm
    template_name='enroll/post.html'
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostView,self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['from'] = context["form"]
        return context


@method_decorator(login_required, name='dispatch')            
class ProfileView(TemplateView):
    template_name='enroll/proflie.html'


class PostSuccessView(TemplateView):
    template_name='enroll/postsuccess.html'


class HomeLoginView(TemplateView):
    template_name='enroll/homelogin.html'


class PostListView(ListView):
    # send_mail_without()
    send_mail_task.delay()
    # sleepy(10)
    # sleepy.delay(10)    
    # signals use
    signals.notification.send(sender=Post,title="hello")
    model = Post
    template_name='enroll/postlist.html'
    ordering=['-created_at']
    paginate_by = 3
       
class Multiplefielddata(CreateView):
    model = Multiplefield
    form_class = MultiplefieldFrom
    template_name='enroll/multiplefield.html'
    success_url = '/'
   
       
def add_show(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        name=request.POST.get("name")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        em=Myfrom(email=email,name=name,lastname=lastname,password=password)
        em.save()
    return render(request, 'enroll/fromexample.html')
    # if request.method=='POST':
    #     import pdb;pdb.set_trace()
    #     email=request.POST['email']
    #     name=request.POST['name']
    #     lastname=request.POST['lastname']
    #     password=request.POST['passwords']
    #     em=Myfrom.objects.create(email=email,name=name,lastname=lastname,password=password)
    #     # em.save()
    #     messages.success(request,'Data has been submitted')
    # return render(request,'enroll/fromexample.html')


class MyPostView(ListView):
    model = Post
    template_name='enroll/postlist.html'
    ordering=['-created_at']
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDetailView(DetailView):
    # send_mail_taskdetails()
    model = Post
    template_name='enroll/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'post'
    


class UpdateView(UpdateView):
    model = Post
    template_name='enroll/update.html'
    fields = ["title","image","description","likes"]
    success_url ="/"
    def form_valid(self, form):
        return super(UpdateView, self).form_valid(form)


class DeleteView(DeleteView):
    model = Post
    template_name='enroll/delete.html'
    success_url ="/"


def like_post(request):
    user=request.user
    if request.method == 'POST':
        post_id=request.POST.get('post_id')
        post_obj=Post.objects.get(id=post_id)
        post_if=post_obj.likes.all()
        if user in post_if:
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)
        like, created = Like.objects.get_or_create(user=user,post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else :
                like.value = 'Like'
        like.save()
        data = {
            'value': like.value,
            'likes': post_obj.likes.all().count(),
            # 'post_user':",".join(str(i) for i in post_if),
        }
        return JsonResponse(data, safe=False)
    return redirect("/")


def add_comment(request):
    if request.method == "POST":
        comment=request.POST.get('body')
        postSno =request.POST.get('post_id')
        post_obj= Post.objects.get(id=postSno)   
        user=request.user
        cm=Comment(post=post_obj,user=user,body=comment)
        cm.save()
        data = Comment.objects.values()
        commdata=data[len(data)-1]
        data = {
            'datas' :commdata,
            'users':request.user.username
        }
        return JsonResponse(data)
    else:
        return HttpResponseRedirect('/home')

    return redirect("/")

from django.core.cache import cache
# ********** redis use *************
def Post_data(request):
    payload=[]
    db=None
    if cache.get("key"):
        payload= cache.get("key")
        db='redis'
        # information redis time 
        print(cache.ttl("key"))

    else:
        post_data=Post.objects.all()
        for i in post_data:
            payload.append(i.title)
            # redis time set 
        cache.set("key",payload,timeout=22)
        db='postgres'

    return JsonResponse({'data':payload,'db':db})