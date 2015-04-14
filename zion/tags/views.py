from django.shortcuts import render
from zion.tags.models import Tag
from zion.forums.views import to_pages


def show_hot_keywords(request):
    
    taglist = Tag.objects.order_by('-article_count').all()
    size = len(taglist)
    one_fifth = size / 5
    two_fifth = one_fifth * 2
    three_fifth = one_fifth * 3
    four_fifth = one_fifth * 4
    
    taglist1 = taglist[0:one_fifth]
    taglist2 = taglist[one_fifth : two_fifth]
    taglist3 = taglist[two_fifth : three_fifth]
    taglist4 = taglist[three_fifth : four_fifth]
    taglist5 = taglist[four_fifth : size]
    
    
    return render(request,'hot_keywords.html',
                  { 'user': request.user,
                    'taglist1': taglist1,
                    'taglist2': taglist2,
                    'taglist3': taglist3,
                    'taglist4': taglist4,
                    'taglist5': taglist5,
                  })

def show_new_keywords(request):
    taglist = Tag.objects.order_by('-proposed_date').all()
    size = len(taglist)
    one_fifth = size / 5
    two_fifth = one_fifth * 2
    three_fifth = one_fifth * 3
    four_fifth = one_fifth * 4
    
    taglist1 = taglist[0:one_fifth]
    taglist2 = taglist[one_fifth : two_fifth]
    taglist3 = taglist[two_fifth : three_fifth]
    taglist4 = taglist[three_fifth : four_fifth]
    taglist5 = taglist[four_fifth : size]
    
    return render(request,'new_keywords.html',
                  { 'user': request.user,
                    'taglist1': taglist1,
                    'taglist2': taglist2,
                    'taglist3': taglist3,
                    'taglist4': taglist4,
                    'taglist5': taglist5,
                  })

def show_all_keywords(request):
    taglist = Tag.objects.order_by('keyword').all()
    size = len(taglist)
    one_fifth = size / 5
    two_fifth = one_fifth * 2
    three_fifth = one_fifth * 3
    four_fifth = one_fifth * 4
    
    taglist1 = taglist[0:one_fifth]
    taglist2 = taglist[one_fifth : two_fifth]
    taglist3 = taglist[two_fifth : three_fifth]
    taglist4 = taglist[three_fifth : four_fifth]
    taglist5 = taglist[four_fifth : size]
    
    return render(request,'all_keywords.html',
                  { 'user': request.user,
                    'taglist1': taglist1,
                    'taglist2': taglist2,
                    'taglist3': taglist3,
                    'taglist4': taglist4,
                    'taglist5': taglist5,
                  })


def page_display(keyword, page):
    if page < 1:
        raise Http404
    tag = Tag.objects.get(keyword=keyword)
    tagged_articles = tag.articles.all()
    article_count = tagged_articles.count()
    page_count = to_pages(article_count) 
    
    start = 20 * (page - 1)
    curr_list = tagged_articles[start:start+20]
    return {'count': page_count, 'curr':curr_list, 'article_count':article_count}


def show_tagged_articles(request, keyword, page=1):
    try:
	    page = int(page)
    except ValueError:
        raise Http404


    pages = page_display(keyword, page)

    return render(request, 
                  'keyword_articles.html',
                  { 'user':request.user,
                    'keyword': keyword,
                    'article_count': pages['article_count'],
                    'page':page,
                    'prev_page':page - 1,
                    'next_page':page + 1,
                    'page_count':pages['count'],
                    'curr_list':pages['curr'],
                  })

