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

    def post(self, request):
        user = request.user
        if user.is_autheticated():
            Token.delete()
        else:
            print(Token.key)
        return Response('delete token')
