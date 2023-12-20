from django.shortcuts import render

from .models import Post,Banner
# Create your views here.


def home(req):
    postSnapshots = Post.objects.all().order_by('-date_published').values()
    bannerSnapshots = Banner.objects.all().values()
    for x in bannerSnapshots:
        x['body']=x['body'][0:50]
    for x in postSnapshots:
        x['body']=x['body'][0:60]
     

    return render(req,'index.html',{'posts':postSnapshots,'banners':bannerSnapshots})


def read(req,slug):
    post = Post.objects.get(slug = slug)
    posts = Post.objects.all().order_by('-date_published').values()
    return render(req,'read.html',{'datum':post,'data':posts})