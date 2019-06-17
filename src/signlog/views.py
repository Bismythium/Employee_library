from django.shortcuts import render
from .forms import SiteuserLoginForm, SiteuserSignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def pagesignup(request):
    emailvalue=''
    uservalue=''
    passwordvalue1=''
    passwordvalue2=''

    form= SiteuserSignupForm(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        emailvalue= form.cleaned_data.get("email")
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password")
        passwordvalue2= form.cleaned_data.get("confirm_password")
        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'signlog/signup.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(uservalue, password= passwordvalue1,
                                           email=emailvalue)
                user.save()


                login(request,user)

                fs.user= request.user

                fs.save()
                context= {'form': form}
                return render(request, 'signlog/signup.html', context)
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'signlog/signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'signlog/signup.html', context)

def pagelogin(request):
  
    uservalue=''
    passwordvalue=''

    form= SiteuserLoginForm(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'homepage.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'signlog/login.html', context )

    else:
        context= {'form': form}
        return render(request, 'signlog/login.html', context)