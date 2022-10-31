
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('login/<username>',views.login_ref,name="login_ref"),
    path('signup/<id>',views.signup,name="signup"),
    path('signup_ref',views.signup_ref,name="signup_ref"),
]
