from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from zion.signin.forms import SignInForm
from zion.signin.models import User
from django.contrib import auth
from django.forms.util import ErrorList

def form(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                username = User.objects.get(email=cd['user_email']).username
                user = auth.authenticate(username=username, 
                                         password=cd['user_password'])
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
            except User.DoesNotExist:
                pass
            errors = form._errors.setdefault('user_password',ErrorList())
            errors.append(u"User and password don't match.")
                
    else:
        form = SignInForm()
    return render(request, 'signin_form.html', {'form':form})
    
