from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User,auth


def index(request):
    dests = Destination.objects.all()
    user = User()
    user = auth.get_user(request)
    print(user.is_authenticated)
    return render(request,"index.html",{'dests':dests,'user':user })
