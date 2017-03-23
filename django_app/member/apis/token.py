from django.core.exceptions import ObjectDoesNotExist
from rest_auth.views import LogoutView as RestLogoutView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = (
    'LogoutView',
    'DeleteToken',
)


class DeleteToken(APIView):
    """
    POST요청이 오면 request.user가 인증되어 있는 경우, request.auth의 Token을 삭제 (숙제)
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(RestLogoutView):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response({'detail': 'Inavalid token'}, status=status.HTTP_404_NOT_FOUND)

            django_logout(request)

        return Response({"detail": _("Successfully logged out.")},
                        status=status.HTTP_200_OK)
