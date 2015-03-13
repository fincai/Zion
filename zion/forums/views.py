from django.shortcuts import render
from django.http import HttpResponse, Http404
from zion.forums.models import Forum
from zion.articles.models import Article

def page_display(page, forum_id, **kwargs):
    if page < 1:
        raise Http404
    try:
        forum = Forum.objects.get(id=forum_id)
        if 'article_id' in kwargs:
            article = Article.objects.get(id=kwargs.get('article_id', None))
    except Forum.DoesNotExist:
        raise Http404
    except Article.DoesNotExist:
        raise Http404

    start = 20 * (page - 1)
    if 'article_id' in kwargs: 
        page_count = to_pages(article.comments) 
        comment_list = article.comment_set.all()[start:start+20]
        return {'count': page_count, 'list':comment_list,
                'forum':forum, 'article':article}
        
    else:
        page_count = to_pages(forum.articles) 
        article_list = forum.article_set.order_by('-post_date').all()[start:start+20]
        return {'count': page_count, 'list':article_list,
                'forum':forum }


def show_list(request, forum_id, page=1):
    try:
        page = int(page)
    except ValueError:
        raise Http404


    pages = page_display(page, forum_id)

    return render(request, 
                  'article_list.html',
                  { 'user':request.user,
                    'forum':pages['forum'],
                    'page':page,
                    'prev_page':page - 1,
                    'next_page':page + 1,
                    'page_count':pages['count'],
                    'article_list':pages['list'],
                  })


def to_pages(article):
    try:
        article = int(article)
    except ValueError:
        raise Http404

    if article <= 20:
        return 1
    elif article % 20 == 0:
        return article // 20
    else:
        return article // 20 + 1
