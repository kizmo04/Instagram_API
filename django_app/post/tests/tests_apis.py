import os
import random

from django.contrib.auth import get_user_model
from django.urls import NoReverseMatch
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from post.models import Post
from utils.testcase import APITestCaseAuthMixin

User = get_user_model()


class PostAPITest(APITestCaseAuthMixin, APILiveServerTestCase):
    def test_apis_url_exist(self):
        try:
            # reverse('api:post-list')
            # reverse('api:post-detail')
            # PostList
            resolve('/api/post/')
            # PostDetail
            resolve('/api/post/1/')
        except NoReverseMatch as e:
            self.fail(e)

    def test_post_create(self):
        user = self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)

        response = self.create_post()

        # response의 status_code가 201(Created)이어야 함
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('author', response.data)
        self.assertIn('created_date', response.data)

        # response 의 author값 검사
        response_author = response.data['author']
        self.assertIn('pk', response_author)
        self.assertIn('username', response_author)

        # response의 postphoto_set검사
        response_postphoto_set = response.data['photo_list']
        self.assertIsInstance(response_postphoto_set, list)
        for postphoto_object in response_postphoto_set:
            self.assertIn('pk', postphoto_object)
            self.assertIn('photo', postphoto_object)
            self.assertIn('created_date', postphoto_object)


        # 생성후 Post인스턴스가 총 1개여야 함
        self.assertEqual(Post.objects.count(), 1)
        # 생성된 Post인스턴스의 author pk가 테스트시 생성한 User의 pk와 같아야 함
        post = Post.objects.first()
        self.assertEqual(post.author.id, user.id)

    def test_cannot_create_post_without_authentication(self):
        url = reverse('api:post-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.exists(), False)

    def test_post_list(self):
        self.create_user_and_login(self.client)
        num = random.randrange(1, 50)
        self.create_post(num)
        url = reverse('api:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), num)
        # 생성된 response의 author필드가 pk가 아닌 dict형태로 전달되는지 확인
        for item in response.data:
            self.assertIn('author', item)
            item_author = item['author']
            self.assertIn('pk', item_author)
            self.assertIn('username', item_author)

            # response의 postphoto_set검사
            item_postphoto_set = item['photo_list']
            self.assertIsInstance(item_postphoto_set, list)
            for postphoto_object in item_postphoto_set:
                self.assertIn('pk', postphoto_object)
                self.assertIn('photo', postphoto_object)
                self.assertIn('created_date', postphoto_object)


def test_post_update_partial(self):
    pass


def test_post_update(self):
    pass


def test_post_retrieve(self):
    pass


def test_post_destroy(self):
    pass


class PostPhotoTest(APITestCaseAuthMixin, APILiveServerTestCase):
    def test_photo_add_to_post(self):
        user = self.create_user_and_login(self.client)

        response = self.create_post()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.author, user)

        url = reverse('api:photo-create')

        file_path = os.path.join(os.path.dirname(__file__), 'img2.gif')
        with open(file_path, 'rb') as fp:
            data = {
                'post': post.pk,
                'photo': fp,
            }
            response = self.client.post(url, data)

        # status_code 확인
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # key 확인
        self.assertIn('post', response.data)
        self.assertIn('photo', response.data)
        # value 확인
        self.assertEqual(post.id, response.data['post'])

    def test_cannot_photo_add_to_post_without_authentication(self):
        pass

    def test_cannot_photo_add_to_post_user_is_not_author(self):
        pass
