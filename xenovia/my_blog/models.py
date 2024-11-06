from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(default=None,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now,blank=True) 
    
    def __str__(self):
        return self.item
    
class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(PostModel, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.content
    
class UserDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    phone = models.IntegerField()
    birthday = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class CategoryDetail(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.description