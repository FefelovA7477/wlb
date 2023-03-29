from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from user.services import get_or_create_user

User = get_user_model()

class TgUserMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        # tg_chat_id = request.META.get('HTTP_TG_CHAT_ID', '')
        # if tg_chat_id == '' \
        #         or not request.user \
        #         or request.user.username != 'tg_bot':
        #     print(request.user)
        #     # request._force_auth_user = AnonymousUser()
        #     return self.get_response(request)
        # try:
        #     request._force_auth_user = get_or_create_user(
        #         username=tg_chat_id, 
        #         tg_chat_id=tg_chat_id
        #     )
        # except Exception as e:
        #     raise
        return self.get_response(request)