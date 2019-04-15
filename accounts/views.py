from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 인증&권한:AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationFrom
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == "POST": # 저장
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else : # 입력할 수 있는 폼
        form = CustomUserCreationFrom()
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
    
def user_page(request,id):
    User = get_user_model() # 이렇게 가져와도 됨
    user_info = User.objects.get(id=id)
    return render(request, "accounts/user_page.html",{"user_info":user_info})
    
def follow(request,id):
    User = get_user_model()
    me = request.user # 로그인한 사람
    you = User.objects.get(id=id) # 팔로워를 누르려는 사람
    
    if me != you :
        if you in me.followings.all():
            me.followings.remove(you)
            #취소
        else :
            me.followings.add(you)
            #추가
    return redirect('accounts:user_page', id)