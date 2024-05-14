from django.core.exceptions import ObjectDoesNotExist
from typing import Union, List, Optional
from django.db.models import QuerySet

def get_object(objects, **kwargs) -> object:
    try:
        return objects.get(**kwargs)
    except ObjectDoesNotExist:
        raise


def get_all_objects(objects) -> Union[QuerySet, List[object]]:
    return objects.all()


def filter_objects(objects, **kwargs) -> Union[QuerySet, List[object]]:
    return objects.filter(**kwargs)


def get_object_or_none(objects, **kwrags) -> Optional[object]:
    try:
        return objects.get(**kwrags)
    except ObjectDoesNotExist:
        return None
    

def create_object(objects, **kwargs) -> Optional[object]:
    return objects.create(**kwargs)