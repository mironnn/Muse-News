from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_app import views
from rest_app.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_rest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^posts/', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
)
