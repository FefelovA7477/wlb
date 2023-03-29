from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional
from django.db.models import QuerySet

import wlb.cmn_services as cmn_services
import category.services as category_services
import score.services as score_services

User = get_user_model()

# def filter_users(*args, **kwargs) -> QuerySet:
#     return cmn_services._filter_objects(User.objects, *args, **kwargs)


def get_user_or_none(*args, **kwargs) -> Optional[object]:
    return cmn_services._get_object_or_none(User.objects, *args, **kwargs)


def get_or_create_user(*args, **kwargs) -> object:
    try:
        return cmn_services._get_object(User.objects, *args, **kwargs)
    except ObjectDoesNotExist:
        return create_user_with_default_categories(*args, **kwargs)
    

def create_user_with_default_categories(*args, **kwargs) -> object:
    user = cmn_services._create_object(
            User.objects,
            *args,
            **kwargs
        )
    category_services.add_default_categories(user=user)
    return user