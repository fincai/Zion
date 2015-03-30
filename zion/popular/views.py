from django.shortcuts import render
from django.http import HttpResponse, Http404
from zion.articles.models import Article
from zion.forums.views import to_pages


def page_display(page):
    if page < 1:
        raise Http404
    popular_articles = Article.objects.order_by('-likes').all()	
    page_count = to_pages(popular_articles.count()) 
    
    start = 20 * (page - 1)
    curr_list = popular_articles[start:start+20]
    return {'count': page_count, 'curr':curr_list}



def popular_list(request, page=1):
	try:
		page = int(page)
	except ValueError:
		raise Http404


	pages = page_display(page)

	return render(request, 
                  'popular_articles.html',
                  { 'user':request.user,
                    'page':page,
                    'prev_page':page - 1,
                    'next_page':page + 1,
                    'page_count':pages['count'],
                    'curr_list':pages['curr'],
                  })



