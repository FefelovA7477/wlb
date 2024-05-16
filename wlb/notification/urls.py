from rest_framework.urls import path

from .views import NotificationCreateRetreiveUpdate

urlpatterns = [
    path(r'', NotificationCreateRetreiveUpdate.as_view(), name='Create Retreive Update Notification')
]