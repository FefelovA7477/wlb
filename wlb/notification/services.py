from requests.exceptions import HTTPError
from django.db.models import QuerySet
from django.utils import timezone
from typing import List, Any, Tuple

from backend.services import cmn_services
from tg.senders import send_notification_tg
from user.services import filter_users
from .models import Notification

manager = Notification.objects


def notify() -> Tuple[List[object], List[object]]:
    """
    :return: Tuple contains 2 lists: 1st - notified users, 
                2nd - users with failed notification
    """
    users = _get_users_for_notification()
    notified_users, unnotified_users = [], []
    for user in users:
        try:
            _notify_user(user=user)
            notified_users.append(user)
        except HTTPError:
            unnotified_users.append(user)
    return (notified_users, unnotified_users)


def _notify_user(user: object) -> None:
    send_notification_tg(chat_id=user.chat_id)
    

def _get_users_for_notification() -> QuerySet | List[Notification]:
    current_time = timezone.now()
    current_time = timezone.datetime(2024, 11, 5, 14)
    delta = timezone.timedelta(minutes=1)
    left_time_boundary, right_time_boundary = current_time.time(), (current_time + delta).time()
    users = filter_users(notifications__time__gte=left_time_boundary,
                         notifications__time__lte=right_time_boundary)\
                            .distinct()
    return users


def get_notification(user: object, **kwargs) -> Notification:
    return cmn_services.get_object(manager, user=user, **kwargs)


def filter_notifications(**kwargs):
    return cmn_services.filter_objects(manager, **kwargs)


def create_notification(**kwargs) -> Notification:
    return cmn_services.create_object(manager, **kwargs)