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
from bootstrap_modal_forms.generic import BSModalCreateView


# class Signup_view(CreateView):
    
#     model = User
#     form_class = SignupForm
#     template_name = 'usermodel/signup.html'

#     def get_form_kwargs(self):
#         kwargs = super(Signup_view, self).get_form_kwargs()
#         return kwargs

#     def form_invalid(self, form):
#         return HttpResponseRedirect(reverse('usermodel:signup'))
        
#     def form_valid(self, form):
#         form.cleaned_data()
#         return HttpResponseRedirect(reverse('core:submitdataframe'))


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
            
            return HttpResponseRedirect(reverse('core:submitdataframe'))
        else:
            return render(request, 'usermodel/signup.html', {'form':form})    
    elif request.method == 'GET':
        form = SignupForm()
        return render(request, 'usermodel/signup.html', {'form':form})

    else:
        form = SignupForm()
        return render(request, 'usermodel/signup.html', {'form':form})

class SignUpModal(BSModalCreateView):
    template_name = 'usermodel/signupmodal.html'
    form_class = SignupFormModal
    success_message = "success: User Signed Up"
    success_url = reverse_lazy('core:home')
    
    # return HttpResponseRedirect(reverse('usermodel:signup'))


# class MyCustomSignupView():
    # pass

# def signup_view(request):
    # form = MyCustomSignupForm()
    # if form.is_valid():
        # form.save()
    # return render(request, 'usermodel/signup.html', {'form':form})


# def Signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user, created = User.objects.get_or_create(username = username)
#             if created == True:
#                 pass
#                 # TODO - Error username already exists please use a different one or try to login
#             else:
#                 user.set_unusable_password()
#                 user.save()
#             # user = authenticate(username=username, password=raw_password)
#             # user.set_unusable_password()
#             # user.save()
#             # login(request, user)
#             return redirect('core:home')
#         else:
#             print(form.errors)
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/signup.html', {'form': form})