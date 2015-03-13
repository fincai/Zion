from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import auth
from zion.forums.models import Forum
from zion.articles.models import Article
from zion.comments.models import Comment
from zion.signin.models import User

def index(request):
    list1 = Forum.objects.filter(topic='Topic1')
    list2 = Forum.objects.filter(topic='Topic2')
    list3 = Forum.objects.filter(topic='Topic3')

    latest_articles = Article.objects.order_by('-post_date').all()[:10]
    
    return render(request, 'index.html', 
                {'user':request.user,
                 'topic1_forumlist': list1,
                 'topic2_forumlist': list2,
                 'topic3_forumlist': list3,
                 'latest_articles': latest_articles,
                 'article_count': Article.objects.count(),
                 'comment_count': Comment.objects.count(),
                 'user_count': User.objects.count(),

                })

def signout(request):
    if request.method == 'POST':
        auth.logout(request) 
        return HttpResponseRedirect('/')
    else:
        return Http404

