from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from zion.register.forms import UserRegisterForm
from zion.signin.models import User

def form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            newuser = User.objects.create_user(username=cd['username'],
                                               email=cd['email'],
                                               password=cd['password'])
            newuser.save()
            user = auth.authenticate(username=cd['username'],
                                     password=cd['password'])
            if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
        
    else:
        form = UserRegisterForm()
    return render(request, 'register_form.html', {'form': form})
        
        



