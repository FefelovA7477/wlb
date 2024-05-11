from . models import Metric
from backend.services import cmn_services

manager = Metric.objects

def create_blank_metric(user: object) -> Metric:
    return cmn_services.create_object(manager, user=user)