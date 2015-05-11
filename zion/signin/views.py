from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

@login_required    
def change_signature(request):
    if request.method == 'POST':
        User.objects.filter(id=request.user.id).update(signature=request.POST['signature'])
        return HttpResponseRedirect('/user/chsign/')

    return render(request,
                  'change_signature.html',
                  { 'user':request.user,
                })
@login_required
def change_username(request):
    error_msg = ''
    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST['username'])
            error_msg = 'The username has already been used!'
        except User.DoesNotExist:
            User.objects.filter(id=request.user.id).update(username=request.POST['username'])
            return HttpResponseRedirect('/user/chname/')

    return render(request,
                  'change_username.html',
                  { 'user':request.user,
                    'error':error_msg,
                })

def show_users(request):
    users_list = User.objects.order_by('-follower').all()
    users_count = len(users_list)
    return render(request, 
                  'browse_users.html',
                  {'user':request.user,
                   'users_list':users_list,
                   'users_count':users_count,
                  })

def show_all_users(request):
    users_list = User.objects.order_by('username').all()
    users_count = len(users_list)
    return render(request, 
                  'all_users.html',
                  {'user':request.user,
                   'users_list':users_list,
                   'users_count':users_count,
                  })
