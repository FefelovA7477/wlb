from django.urls import path

from .views import RetrieveUser


urlpatterns = [
    path(r'', RetrieveUser.as_view(), name='Retrieve user'),
]