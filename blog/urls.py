from django.conf.urls import url, include
from . import views
from .forms import PostForm
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myposts/$', views.post_list, name='my_post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    
]