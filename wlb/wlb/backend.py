from rest_framework.authentication import TokenAuthentication, exceptions
from user.services import get_or_create_user

class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
            tg_chat_id = request.META.get('HTTP_TG_CHAT_ID', '')
            if user.username != 'tg_bot':
                msg = 'Аутентификация производится не из бота, а ЦЕ БАН!'
                raise exceptions.AuthenticationFailed(msg)
            if tg_chat_id == '':
                msg = 'Tg-Chat-Id не указан!'
                raise exceptions.AuthenticationFailed(msg)
            
            try:
                user = get_or_create_user(
                    username=tg_chat_id, 
                    tg_chat_id=tg_chat_id
                )
                return (user, None)
            except Exception as e:
                msg = f'Какая-то хуйня полетела, напиши Сане. Ошибка: {e}'
                raise exceptions.AuthenticationFailed(msg)
        except TypeError:
            return None
        except Exception as e:
            raise
