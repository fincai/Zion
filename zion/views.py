from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import auth
from zion.forums.models import Forum

def index(request):
    list1 = Forum.objects.filter(topic='Topic1')
    list2 = Forum.objects.filter(topic='Topic2')
    list3 = Forum.objects.filter(topic='Topic3')
    
    return render(request, 'index.html', 
                {'user':request.user,
                 'topic1_forumlist': list1,
                 'topic2_forumlist': list2,
                 'topic3_forumlist': list3,

                })

def signout(request):
    if request.method == 'POST':
        auth.logout(request) 
        return HttpResponseRedirect('/')
    else:
        return Http404

