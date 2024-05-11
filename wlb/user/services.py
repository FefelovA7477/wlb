from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional

import category.services as category_services
from stats.services import create_blank_metric
from backend.services import cmn_services

User = get_user_model()

def get_user(**kwargs) -> object:
    return cmn_services.get_object(User.objects, **kwargs)


def get_or_create_user(**kwargs) -> object:
    try:
        user = cmn_services.get_object(User.objects, **kwargs)
        if user.is_new:
            user.is_new = False
            user.save()
        return user
    except ObjectDoesNotExist:
        return create_user(**kwargs)
    

def create_user(**kwargs) -> object:
    user = cmn_services.create_object(
        User.objects,
        **kwargs
    )
    _create_and_set_default_categories_for_user(user)
    _create_blank_metric_for_user(user)
    return user


def _create_and_set_default_categories_for_user(user: object) -> None:
    default_categories = category_services.create_default_categories()
    user.categories.add(*default_categories)
    user.save()

def _create_blank_metric_for_user(user: object) -> None:
    return create_blank_metric(user=user)
