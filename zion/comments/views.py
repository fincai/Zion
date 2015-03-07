from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from zion.comments.forms import NewCommentForm
from zion.forums.models import Forum
from zion.articles.models import Article
from zion.comments.models import Comment
from zion.articles.views import article_detailview


def new_comment(request, forum_id, article_id, page=1):
    try:
        forum = Forum.objects.get(id=forum_id)
        article = Article.objects.get(id=article_id)
    except Forum.DoesNotExist:
        raise Http404
    except Article.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if request.POST.has_key('full'):
            return render(request, 'new_comment_full.html', 
                    {'user':request.user, 
                     'form':form,
                     'forum':forum,
                     'article':article,
                    }) 

        if form.is_valid():
            cd = form.cleaned_data
            comment = Comment.objects.create(post_date=datetime.now(),
                                   poster=request.user,
                                   article=article,
                                   text=cd['comment'])
            Article.objects.filter(id=article_id).update(comments = article.comments + 1)
            #return article_detailview(request, forum_id, article_id, page, comment_success=True)
            return HttpResponseRedirect('/forum/{0}/article/{1}/new_comment/success/#comment-{2}'. \
                                   format(forum_id, article_id, comment.id))

        elif request.POST.has_key('full_request'):
            return render(request, 'new_comment_full.html', 
                            {'user':request.user, 
                             'form':form,
                             'forum':forum,
                             'article':article,
                            }) 
        else:
            return article_detailview(request, forum_id, article_id, page, error_form=form)
            
    else:  # Not post
        raise Http404
    

    
def success_comment(request, forum_id, article_id, page=1):
    return article_detailview(request, forum_id, article_id, page, comment_success=True)
    
