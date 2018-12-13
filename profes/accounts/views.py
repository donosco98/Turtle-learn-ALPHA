from django.shortcuts import render,redirect
from django.contrib.auth import(
    authenticate,get_user_model,login,logout,


)
from .forms import UserLoginForm

# Create your views here.
def login_view(request):
    form=UserLoginForm(request.POST or None)


    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)


        login(request,user)
        print(request.user.is_authenticated)
        return redirect("http://127.0.0.1:8000/list/")
    return render(request,"register.html",{'form':form})


def register_view(request):
    return render(request,"register.html",{})

def logout_view(request):

    logout(request)
    return render(request,"register.html",{})
