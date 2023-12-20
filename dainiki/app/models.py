from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date_published = models.DateTimeField(default = timezone.now)
    # comment = models.ForeignKey(Comment,on_delete = models.CASCADE,default ="",null = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    relevant_image = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    comment_counter = models.PositiveIntegerField(default = 0)
    like_counter = models.PositiveIntegerField(default = 0)
    share_counter = models.PositiveIntegerField(default = 0)
    slug = models.SlugField(default = "",null = False)

    def __str__(self):
        return f"{self.title}"


class Banner(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    relevant_image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    text = models.CharField(max_length = 200)
    Commenter = models.ForeignKey(User,on_delete = models.CASCADE)
    date_commented = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)


    def __str__(self):
        return f"{self.id}"