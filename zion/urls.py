from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zion',
    # Examples:
    # url(r'^$', 'zion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'views.index'),
    url(r'^register/$', 'register.views.form'),
    url(r'^signin/$', 'signin.views.form'),
    url(r'^signout/$', 'views.signout'),

    url(r'^forum/(?P<forum_id>[1-9])/$', 'forums.views.show_list'),
    url(r'^forum/(?P<forum_id>[1-9])/page/(?P<page>\d+)/$', 'forums.views.show_list'),

    url(r'^forum/(?P<forum_id>[1-9])/new_post/$', 'articles.views.new_post'),
    url(r'^forum/(?P<forum_id>[1-9])/article/(?P<article_id>\d+)/$', 'articles.views.article_detailview'),
    url(r'^forum/(?P<forum_id>[1-9])/article/(?P<article_id>\d+)/page/(?P<page>\d+)/$', 
         'articles.views.article_detailview'),

    url(r'^forum/(?P<forum_id>[1-9])/article/(?P<article_id>\d+)/new_comment/$', 'comments.views.new_comment'),
    url(r'^forum/(?P<forum_id>[1-9])/article/(?P<article_id>\d+)/new_comment/success/$', 'comments.views.success_comment'),

    url(r'^forum/(?P<forum_id>[1-9])/article/(?P<article_id>\d+)/thumbup/$', 'articles.views.flip_thumb'),

    url(r'^user/(?P<user_id>\d+)/$', 'profiles.views.show_articles'),
    #url(r'^user/(?P<user_id>\d+)/comments/$', 'profiles.views.show_comments'),
    url(r'^user/(?P<user_id>\d+)/follows/$', 'profiles.views.show_follows'),
    url(r'^user/(?P<user_id>\d+)/followers/$', 'profiles.views.show_followers'),

    url(r'^user/(?P<user_id>\d+)/follow/$', 'profiles.views.follow_action'),

    url(r'^user/chavatar/$', 'avatar.views.change_avatar'),
    url(r'^user/chavatar/upload/$', 'avatar.views.upload'),
    url(r'^user/chavatar/upload/crop/$', 'avatar.views.crop'),

)
