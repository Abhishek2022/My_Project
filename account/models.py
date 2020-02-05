from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# class Feed(models.Model):
#     name = models.CharField(max_length=80)
#     no_of_followers = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

class Profile(models.Model):
    name    = models.CharField(max_length=80)
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200)
    bio     = models.CharField(max_length=150, blank=True, null=True)
    dob     = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.username
    
# class Post(models.Model):
#     caption = models.CharField(max_length=200)
#     image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=10)
#     people = models.CharField(max_length=300)
#     post_date = models.DateField(auto_now=False, auto_now_add= False, default=datetime.now())

# class Comment(models.Model):
#     post = models.ForeignKey('Post', on_delete= models.CASCADE)
#     text = models.TextField()
#     create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    


