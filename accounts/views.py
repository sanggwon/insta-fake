from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 인증&권한:AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == "POST": # 저장
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else : # 입력할 수 있는 폼
        form = UserCreationForm()
    return render(request,"accounts/form.html",{"form":form})
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("posts:list")
    else :
        form = AuthenticationForm()
    
    return render(request,"accounts/form.html", {"form":form})

def logout(request):
    auth_logout(request)
    return redirect("posts:list")