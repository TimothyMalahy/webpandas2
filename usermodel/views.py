from django.contrib.auth.hashers import make_password
from usermodel.models import User
from django.http.response import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DetailView, TemplateView
from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.debug import sensitive_post_parameters, sensitive_variables
from django.contrib.auth import authenticate

@sensitive_variables('password','passwordconf')
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)
            user = authenticate(email=email, password=password)
            
            return HttpResponseRedirect(reverse('core:submitdataframe'))
        else:
            return render(request, 'usermodel/signup.html', {'form':form})    
    elif request.method == 'GET':
        form = SignupForm()
        return render(request, 'usermodel/signup.html', {'form':form})

    else:
        form = SignupForm()
        return render(request, 'usermodel/signup.html', {'form':form})

def signin_view(request):
    context = {
        'form':MyLoginForm(),
    }
    return render(request, 'usermodel/signin.html', context)


def signup_view2(request):
    context = {
        'form':MySignupForm(),
    }
    return render(request, 'usermodel/signup2.html', context)