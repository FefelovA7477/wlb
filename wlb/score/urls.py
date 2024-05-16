from rest_framework.urls import path

from .views import ScoreCRUD

urlpatterns = [
    path(r'', ScoreCRUD.as_view(), name='Score CRUD')
]