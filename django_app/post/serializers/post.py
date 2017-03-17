from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post

# from . import PostPhotoSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    # photo_list = PostPhotoSerializer(source='postphoto_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
        )
        read_only_fields = (
            'created_date',
        )
