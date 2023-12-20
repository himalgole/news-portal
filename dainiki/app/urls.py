from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('read/<slug:slug>',views.read,name='read'),
]