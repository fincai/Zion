from django.shortcuts import render

def show_articles(request):
    return render(request,'tagged_articles.html',
                  { 'user': request.user,

                  })
