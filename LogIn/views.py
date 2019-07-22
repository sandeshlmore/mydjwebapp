from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
global user
user = User()
def homepage(request):
    user = auth.get_user(request)
    print(user.is_authenticated)
    return render(request,"index.html", {'user':user })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            print("user logged in")
            auth.login(request,user)
            user = auth.get_user(request)
            print(user.is_authenticated)
            return redirect('/', {'user':user})
        else:
            print("invalid user")
            messages.info(request,'INVALID USER')
            return redirect('/loginform.html')
    else:
        return render(request, 'loginform.html')

def logout(request):
    user = auth.get_user(request)
    print(user.is_authenticated)
    auth.logout(request)
    return redirect('/', {'user':user})