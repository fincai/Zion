from django.shortcuts import render
from django.http import Http404, HttpResponse
from django_ajax.decorators import ajax
from zion.signin.models import User
from zion.articles.models import Article

def show_articles(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    article_list = Article.objects.filter(author_id=user_id).all()
    

    is_following = True
    count = user.fans_set.filter(id=request.user.id).count()
    if count == 0:
        is_following = False

    return render(request, 
                  'user_profile.html',
                  {'user':request.user,
                   'profile_user':user,
                   'article_list':article_list,
                   'is_following':is_following,
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

@ajax
def follow_action(request, user_id):
    if request.user.is_authenticated and request.method == 'POST' and request.user.id != user_id:
        if request.POST['action'] == 'follow':
            followed_user = User.objects.get(id=user_id)
            followed_user.fans_set.add(request.user)
            User.objects.filter(id=user_id).update(follower = followed_user.fans_set.count())

            request.user.follows_set.add(followed_user)
            User.objects.filter(id=request.user.id).update(following = request.user.follows_set.count())
            return {'action_complete' : 1}

        elif request.POST['action'] == 'unfollow':
            unfollowed_user = User.objects.get(id=user_id)
            unfollowed_user.fans_set.remove(request.user)
            User.objects.filter(id=user_id).update(follower = unfollowed_user.fans_set.count())

            request.user.follows_set.remove(unfollowed_user)
            User.objects.filter(id=request.user.id).update(following = request.user.follows_set.count())
            
            return {'action_complete' : 1}
        else:
            return {'action_complete' : 0}
    else:
        return Http404
