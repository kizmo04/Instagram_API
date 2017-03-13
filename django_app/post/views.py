from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from post.models import Post, PostPhoto

User = get_user_model()


@csrf_exempt
def post_create(request):
    if request.method == 'POST':
        try:
            author_id = request.POST.get('author_id')
            author = User.objects.get(id=author_id)
        except KeyError:
            return HttpResponse('key "author_id" is required field')
        except User.DoesNotExist:
            return HttpResponse('author_id:{} is not exist'.format(
                request.POST['author_id']
            ))

        post = Post.objects.create(author=author)
        return HttpResponse('{}'.format(post.pk))
    else:
        return HttpResponse('Post-create view')


@csrf_exempt
def post_photo_add(request):
    if request.method == 'POST':
        try:
            post_id = request.POST.get('post_id')
            photo = request.FILES.get('photo')
            post = Post.objects.get(id=post_id)
        except KeyError:
            return HttpResponse('post_id and photo is required fields')
        except Post.DoesNotExist:
            return HttpResponse('post_id {} is not exist'.format(
                request.POST['post_id']
            ))
        PostPhoto.objects.create(
            post=post,
            photo=photo
        )
        return HttpResponse('Post:{}, PhotoList:{}'.format(
            post.id,
            [photo.id for photo in post.postphoto_set.all()]
        ))
    else:
        return HttpResponse('post-photo-add view')
