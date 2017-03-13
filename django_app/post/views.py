from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from post.models import Post, PostPhoto

User = get_user_model()


def post_list(request):
    # post_list = Post.objects.select_related('author')
    # post_dict_list = []
    # cur_post_photo_dict_list = []
    # for post in post_list:
    #     cur_post_dict = {
    #         'pk': post.pk,
    #         'photo_list': cur_post_photo_dict_list,
    #         'created_date': post.created_date,
    #         'author': {
    #             'pk': post.author.pk,
    #             'username': post.author.username,
    #         },
    #     }
    #
    #     cur_post_photo_list = post.postphoto_set.all()
    #     cur_post_photo_dict_list = []
    #     for post_photo in cur_post_photo_list:
    #         cur_post_photo_dict = {
    #             'pk': post_photo.pk,
    #             'photo': post_photo.photo.url,
    #         }
    #         cur_post_photo_dict_list.append(cur_post_photo_dict)
    #
    #     post_dict_list.append(cur_post_dict)

    context = {
        "post_list": [post.to_dict() for post in Post.objects.all()]
    }
    return JsonResponse(data=context)


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
