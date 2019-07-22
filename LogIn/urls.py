from django.urls import path,include
from . import views
urlpatterns = [

    path('loginform.html/', views.login),
    path('loginform.html/login', views.login),
    path('logout',views.logout),
    #path('',views.homepage)
]