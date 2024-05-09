from typing import Optional

import wlb.cmn_services as cmn_services
from .models import Category

def get_category(*args, **kwargs) -> Optional[Category]:
    return cmn_services._get_object(Category.objects, *args, **kwargs)


def create_category(*args, **kwargs) -> Category:
    return cmn_services._create_object(Category.objects, *args, **kwargs)


def add_default_categories(user, *args, **kwrags) -> None:
    return Category.objects.add_default_categories(user=user)


def filter_categories(*args, **kwrags) -> None:
    return cmn_services._filter_objects(Category.objects, *args, **kwrags)


def set_category_activity(category: Category, state: bool) -> None:
    category.is_active = state
    category.save()