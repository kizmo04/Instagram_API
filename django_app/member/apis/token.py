from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = (
    'DeleteToken',
)


class DeleteToken(APIView):
    """
    POST요청이 오면 request.user가 인증되어 있는 경우, request.auth의 Token을 삭제 (숙제)
    """
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        user = request.user
        if user:
            request.auth.delete()
            token = Token.objects.get()
            print(type(token))
            print('before' + token.key)
            token.delete()
            print(type(token))
            return Response('token deleted')
        else:
            print(request.auth)
        return Response('뀨')
