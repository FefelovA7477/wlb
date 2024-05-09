from django.urls import path

from .views import ListCreateScore, RetrieveUpdateDestroyScore


urlpatterns = [
    path(r'', ListCreateScore.as_view(), name='List & create score'),
    path(r'<int:id>/', 
         RetrieveUpdateDestroyScore.as_view(), 
         name='Retrieve & update & destroy score'),
]