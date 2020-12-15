from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('puppies',views.puppies),
    path('register',views.register),
    path('login',views.login),
    path('adminpage',views.adminpage),
    path('adddog',views.adddog),
    path('addpup',views.addpup),
    path('contactus',views.contactpage),
    path('gallery',views.gallery),
    path('adopt',views.adoptpage),
    path('submitted',views.submit_app),
    path('success',views.success)
]