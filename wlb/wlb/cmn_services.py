from django.core.exceptions import ObjectDoesNotExist
from typing import Union, List, Optional, Callable
from django.db.models import QuerySet

def _get_object(objects, *args, **kwargs) -> object:
    try:
        return objects.get(*args, **kwargs)
    except ObjectDoesNotExist:
        raise


def _get_all_objects(objects) -> Union[QuerySet, List[object]]:
    return objects.all()


def _filter_objects(objects, *args, **kwargs) -> Union[QuerySet, List[object]]:
    return objects.filter(*args, **kwargs)


def _get_object_or_none(objects, *args, **kwrags) -> Optional[object]:
    try:
        return objects.get(*args, **kwrags)
    except ObjectDoesNotExist:
        return None
    

def _create_object(objects, *args, **kwargs) -> Optional[object]:
    return objects.create(*args, **kwargs)