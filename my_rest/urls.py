from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_app import views
from rest_app.views import index, UserListAPIView

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
    url(r'^auth/', include('login.urls')),

#    url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
#    url(r'api/v1/users/', UserListAPIView.as_view()),

    url(r'^.*$', TemplateView.as_view(template_name='index.html')),

)
