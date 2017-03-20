from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from post.models import Post
from post.models import PostComment

__all__ = (
    'CommentCreate',
)


@method_decorator(login_required, name='dispatch')
class CommentCreate(View):
    def post(self, request, *args, **kwargs):
        post_pk = kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        content = request.POST['content']
        author = request.user
        PostComment.objects.create(
            post=post,
            author=author,
            content=content,
        )
        return redirect('post:post-detail', pk=post_pk)
