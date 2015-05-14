from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from zion.signin.forms import SignInForm, ChangeEmailForm, ChangePasswordForm
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
                
@login_required
def change_email(request):
    error_msg = ''
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                User.objects.get(email=request.POST['email'])
                error_msg = 'The email has already been registered!'
            except User.DoesNotExist:
                User.objects.filter(id=request.user.id).update(email=request.POST['email'])
                return HttpResponseRedirect('/user/chemail/')
    else:
        form = ChangeEmailForm()

    return render(request,
                    'change_email.html',
                    { 'user':request.user,
                      'form':form,
                      'duplicate_error': error_msg,
                })

@login_required
def change_password(request):
    reset_result = ''
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if request.user.password == request.POST['password']:
                reset_result = 'The new password cannot be the same as the old one'
            else:
                User.objects.filter(id=request.user.id).update(password=request.POST['password'])
                reset_result = 'Password has been reset successfully.'
    else:
        form = ChangePasswordForm()

    return render(request,
                    'change_email.html',
                    { 'user':request.user,
                      'form':form,
                      'reset_result': reset_result,
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
