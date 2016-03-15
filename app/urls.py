from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.detail, name = 'post'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name = 'category'),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag, name = 'tag'),
]