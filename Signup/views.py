from django.shortcuts import render,redirect
from .forms import Signup_Form
from django.contrib import messages

def Signup_views(request):
    if request.method=="POST":
        form=Signup_Form(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,'Your account has been created. Now you can login using your username and password.')
            return redirect('login')
    return render(request,"Signup.html",{'form':Signup_Form})