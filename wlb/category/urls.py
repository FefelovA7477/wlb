from django.urls import path

from .views import RetrieveUpdateDestroyCategory, ListCreateCategory


urlpatterns = [
    path(r'', ListCreateCategory.as_view(), name='List & create category'),
    path(r'<int:id>/', 
         RetrieveUpdateDestroyCategory.as_view(), 
         name='Retrieve & update & destroy category'),
]