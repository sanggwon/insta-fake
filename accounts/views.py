from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    if request.method == "POST": # 저장
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else : # 입력할 수 있는 폼
        form = UserCreationForm()
    return render(request,"accounts/signup.html",{"form":form})
