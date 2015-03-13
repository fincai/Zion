from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ajax.decorators import ajax
from zion.articles.forms import NewArticleForm
from zion.comments.forms import NewCommentForm
from zion.signin.models import User
from zion.forums.models import Forum
from zion.articles.models import Article
from zion.comments.models import Comment
from zion.forums.views import page_display

def new_post(request, forum_id):
    try:
        forum = Forum.objects.get(id=forum_id) 
    except Forum.DoesNotExist:
        return Http404
        
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Article.objects.create(forum=forum,
                                   title=cd['name'].strip(),
                                   author=request.user,
                                   text=cd['body'],
                                   post_date=datetime.now())
            Forum.objects.filter(id=forum_id).update(articles = forum.articles + 1)
            User.objects.filter(id=request.user.id).update(articles = request.user.articles + 1)
            return HttpResponseRedirect('/forum/{0}/'.format(forum_id))

    else:
        form = NewArticleForm()

    return render(request, 
                  'new_article_form.html',
                  {'user': request.user,
                   'forum_id': forum.id,
                   'forum_topic': forum.topic,
                   'forum_name': forum.name,
                   'form': form,
                  })
                
def article_detailview(request, forum_id, article_id, page=1, **kwargs):
    try:
        page = int(page)
    except ValueError:
        raise Http404

    pages = page_display(page, forum_id, article_id=article_id)

    comment_form = NewCommentForm()

    if 'error_form' in kwargs:
        comment_form = kwargs['error_form']
    if 'comment_success' in kwargs:
        is_success = True 
        page = pages['count']
        pages = page_display(page, forum_id, article_id=article_id)
        
    else:
        is_success = False

    
        

    been_commented = True 
    if request.user.is_authenticated:
        try:
            Comment.objects.get(poster_id=request.user.id, article_id=pages['article'].id) 
        except Comment.DoesNotExist:
            been_commented = False
    
    

    return render(request,
                  'article_view.html',
                  { 'user': request.user,
                    'form': comment_form,
                    'forum':pages['forum'],
                    'article':pages['article'],
                    'page':page,
                    'prev_page':page - 1,
                    'next_page':page + 1,
                    'page_count':pages['count'],
                    'comment_list':pages['list'],
                    'comment_success':is_success,
                    'been_commented': been_commented,
                  })

@ajax
def flip_thumb(request, forum_id, article_id):
    if request.user.is_authenticated:
        article = Article.objects.get(id=article_id)
        count = article.agreed_users.filter(id=request.user.id).count()
        if count > 0:
            return {'been_agreed': 1}
        else:
            article.agreed_users.add(request.user)
            Article.objects.filter(id=article_id).update(likes = article.agreed_users.count())
            return {'been_agreed': 0, 'likes':article.agreed_users.count()}
