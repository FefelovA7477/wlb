from django.conf import settings

TG_AUTH_KEY = settings.TG_AUTH_KEY

def validate_tg_key(tg_key: str) -> bool:
    return str(tg_key) == str(TG_AUTH_KEY)