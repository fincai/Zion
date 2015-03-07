from django.shortcuts import render
from django.http import Http404, HttpResponse
from zion.signin.models import User
from zion.articles.models import Article

def show_articles(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    article_list = Article.objects.filter(author_id=user_id).all()
    

    return render(request, 
                  'user_profile.html',
                  {'user':request.user,
                   'profile_user':user,
                   'article_list':article_list,
                  })

    
def show_follows(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    follows_list = user.follows_set.all()
    
    return render(request, 
                  'user_follows.html',
                  {'user':request.user,
                   'profile_user':user,
                   'follows_list':follows_list,
                  })
    
def show_followers(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    followers_list = user.fans_set.all()
    
    return render(request, 
                  'user_followers.html',
                  {'user':request.user,
                   'profile_user':user,
                   'followers_list':followers_list,
                  })
