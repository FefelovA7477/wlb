from django.core.exceptions import ObjectDoesNotExist

import wlb.cmn_services as cmn_sevices
from .models import Notification

def temp_get_or_create_notification(*args, **kwargs) -> Notification:
    try:
        cmn_sevices._get_object(Notification.objects, *args, **kwargs)
    except ObjectDoesNotExist:
        return cmn_sevices._create_object(Notification.objects, *args, **kwargs)
    except Exception as e:
        raise


def temp_get_notification(*args, **kwargs) -> Notification:
    try:
        cmn_sevices._get_object(Notification.objects, *args, **kwargs)
    except ObjectDoesNotExist:
        raise