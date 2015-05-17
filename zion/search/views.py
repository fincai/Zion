import re
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from zion.search.forms import SearchFormSimple
from django.db.models import Q
from zion.articles.models import Article
from zion.forums.views import to_pages


def normalize_query(query_string, 
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
            
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
            
                
def search(request, page=1):
	try:
		page = int(page)
	except ValueError:
		raise Http404

    form = SearchFormSimple(request.POST)
    found_articles = None
    curr_list = None
    page_count = 1

    if form.is_valid():
        cd = form.cleaned_data
        query_string = cd['search_query']
        if cd['search_author']:
            search_fields = ['author', 'title', 'text']
        elif cd['search_in_titles'] == True:
            search_fields = ['title']
        else:
        search_fields = ['title', 'text']

        entry_query = get_query(query_string, search_fields)
        found_articles = Article.objects.filter(entry_query).order_by('-post_date')

        page_count = to_pages(found_articles.count()) 
        start = 20 * (page - 1)
        curr_list = found_articles[start:start+20]
    else:
        form = SearchFormSimple()
    		
    return render(request,
                'search_articles.html',
                { 'user':request.user,
                  'form':form,
                  'page':page,
                  'prev_page':page - 1,
                  'next_page':page + 1,
                  'page_count':pages_count,
                  'found_articles': curr_list,
                })
