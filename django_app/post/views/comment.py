from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from post.models import Post
from post.models import PostComment

__all__ = (
    'CommentCreate',
)


@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    model = PostComment
    fields = ('content',)

    def get_success_url(self):
        next = self.request.GET.get('next')
        return next if next else reverse('post:post-detail', kwargs={'pk': self.kwargs['post_pk']})

    def form_valid(self, form):
        # author 와 post가 빈 PostComment 객체 생성
        comment = form.save(commit=False)
        post_pk = self.kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        author = self.request.user
        comment.post = post
        comment.author = author
        comment.save()
        return HttpResponseRedirect(self.get_success_url())
