from django.conf.urls import url

from .. import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='photo-delete'),
    url(r'^(?P<pk>[0-9]+)/create/$', views.PostCreate.as_view(), name='photo-create'),

]
