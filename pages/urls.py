from django.urls import path
from pages import views

urlpatterns=[
    path('',views.homepageView.as_view(),name='home'),
    path('about/',views.aboutPageView.as_view(),name='about')
]