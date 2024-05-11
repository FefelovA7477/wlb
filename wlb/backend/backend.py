from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional, Tuple

from user.services import get_user

def get_user_by_chat_id(tg_chat_id: str) -> Optional[object]:
    try:
        return get_user(tg_chat_id=tg_chat_id)
    except ObjectDoesNotExist:
        return None

class TgChatIdAuthentication(BaseAuthentication):
    def authenticate(self, request) -> Optional[Tuple[object, None]]:
        tg_chat_id = request.META.get('HTTP_TG_CHAT_ID', None)
        if tg_chat_id is None:
            return None
        user = get_user_by_chat_id(tg_chat_id=tg_chat_id)
        if user is None:
            raise AuthenticationFailed('User with provided chat_id doesnt exists')
        return (user, None)
