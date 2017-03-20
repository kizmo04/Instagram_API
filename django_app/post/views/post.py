"""
class based view로 PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
"""
from django.views import View
from django.views.generic import ListView

from post.models import Post


class PostList(ListView):
    model = Post


class PostDetail(View):
    pass


class PostCreate(View):
    pass


class PostDelete(View):
    pass