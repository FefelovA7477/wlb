from django.db.models import QuerySet

import wlb.cmn_services as cmn_services
from .models import Score
import category.services as category_services

def get_all_user_scores(user: object, *args, **kwargs) -> QuerySet:
    return filter_scores(
        category__in=category_services.filter_categories(user=user)
    )


def create_score_object(
        score: int, 
        category: object,
        *args,
        **kwargs
    ) -> Score:
    return cmn_services._create_object(
        Score.objects,
        score=score,
        category=category,
        *args,
        **kwargs
    )


def filter_scores(*args, **kwargs):
    return cmn_services._filter_objects(
        Score.objects,
        *args,
        **kwargs
    )


def get_score_object(*args, **kwargs) -> Score:
    return cmn_services._get_object(Score.objects, *args, **kwargs)


