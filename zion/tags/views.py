from django.shortcuts import render
from zion.tags.models import Tag

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
    pass


def show_all_keywords(reqeust):
    pass
