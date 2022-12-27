from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	image =models.ImageField(upload_to ='images/')
	author =models.ForeignKey(User,on_delete= models.CASCADE,blank=True,related_name='postuser')
	description=models.TextField()
	updated_at=models.DateTimeField(auto_now= True)
	created_at=models.DateTimeField(auto_now_add=True)
	likes=models.ManyToManyField(User,blank=True, related_name='likes')
	def __str__(self):
		return self.title
	def likeuser(self):
		return ",".join(str(i) for i in self.likes.all())
	def likeusers(self):
		return self.likes.all().count()   
	

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userlike')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=50)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usercomments')
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
    	return self.body
    # class Meta:
    #     ordering = ['-created']
    
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	moblie=models.CharField(max_length=12)
	def __str__(self):
		return self.user


class Multiplefield(models.Model):
	value = models.CharField(max_length=200)
	def __str__(self):
		return self.value




# created_at__month ====> created_at month find

"""import datetime
>>> x = datetime.datetime.now()
>>> print(x)
2022-11-04 11:39:42.611434
>>> mo=x.strftime("%m")
>>> print(mo)
11
>>> Post.objects.filter(created_at__month=mo)
<QuerySet [<Post: dfas>]>
"""