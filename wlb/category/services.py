from typing import Optional, List

from backend.services import cmn_services
from .models import Category

manager = Category.objects

def get_category(**kwargs) -> Category:
    return cmn_services.get_object(manager, **kwargs)


def create_category(**kwargs) -> Category:
    category_instance = cmn_services.create_object(manager, **kwargs)
    if category_instance.color is None:
        category_instance.set_random_color()
    return category_instance


def create_default_categories() -> List[Category]:
    return manager.clone_default_categories()


def filter_categories(**kwrags):
    return cmn_services.filter_objects(manager, **kwrags)


def set_category_activity(category: Category, state: bool) -> None:
    category.is_active = state
    category.save()