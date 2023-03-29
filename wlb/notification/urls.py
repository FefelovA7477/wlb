from django.urls import path

from .views import CRUDNotification

urlpatterns = [
    path(r'', 
         CRUDNotification.as_view(), 
         name='Actually CRUD. *All cuz of singletone'),
]