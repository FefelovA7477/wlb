from rest_framework.authentication import BaseAuthentication

def get_user():
    pass

def authenticate():
    pass

class BearerTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        tg_chat_id = request.META.get('HTTP_TG_CHAT_ID', '')

        return super().authenticate(request)
