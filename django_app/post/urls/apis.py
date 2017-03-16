from django.conf.urls import url

from post import apis

urlpatterns = [
    url(r'^$', apis.PostList.as_view(), name='post-list'),
]
