from backend.services import cmn_services
from .models import Score
from category import services as category_services

def get_all_user_scores(user: object, **kwargs):
    return filter_scores(
        category__in=category_services.filter_categories(user=user)
    )


def create_score_object(**kwargs) -> Score:
    return cmn_services.create_object(
        Score.objects,
        **kwargs
    )


def filter_scores(*args, **kwargs):
    return cmn_services.filter_objects(
        Score.objects,
        **kwargs
    )


def get_score_object(**kwargs) -> Score:
    return cmn_services.get_object(Score.objects, **kwargs)


