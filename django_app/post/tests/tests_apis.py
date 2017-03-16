from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from post.models import Post

User = get_user_model()


class PostAPITest(APILiveServerTestCase):
    test_username = 'test_username'
    test_password = 'test_password'

    default_date = ''

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def test_apis_url_exist(self):
        reverse('api:post-list')
        reverse('api:post-detail')

    def test_post_create(self):
        user = self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)

        url = reverse('api:post-create')
        data = {
            'author_id': user.id,
        }
        # Post를 생성하는 API주소에 POST요청 response받아옴
        response = self.client.post(url, data)

        # response의 status_code가 201(Created)이어야 함
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 생성후 Post인스턴스가 총 1개여야 함
        self.assertEqual(Post.objects.count(), 1)
        # 생성된 Post인스턴스의 author pk가 테스트시 생성한 User의 pk와 같아야 함
        post = Post.objects.first()
        self.assertEqual(post.author.id, user.id)

    def test_cannot_create_post_not_authenticated(self):
        url = reverse('api:post-create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.exists(), False)

    def test_post_list(self):
        pass

    def test_post_update_partial(self):
        pass

    def test_post_update(self):
        pass

    def test_post_retrieve(self):
        pass

    def test_post_destroy(self):
        pass
