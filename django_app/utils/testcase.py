from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class APITestCaseAuthMixin(object):
    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def create_user_and_login(self, client):
        self.create_user()
        client.login(username=self.test_username, password=self.test_password)

    def create_post(self, num=1):
        url = reverse('api:post-list')
        # Post를 생성하는 API주소에 POST요청 response받아옴
        for i in range(num):
            response = self.client.post(url)
            if num == 1:
                return response
        return response
