from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

#getting user model object
User = get_user_model()


class Post(models.Model):
    '''
    this is a class define posts for blog app
    '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
