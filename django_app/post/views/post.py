"""
class based view로 PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
"""
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from post.models import Post

__all__ = (
    'PostList',
    'PostDetail',
    'PostCreate',
    'PostDelete',
)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post


class PostCreate(View):
    pass


class PostDelete(View):
    pass
