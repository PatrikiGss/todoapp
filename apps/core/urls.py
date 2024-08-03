# core/urls.py
from django.urls import path # type: ignore
from .views import HomeView, SearchTasksView

app_name = 'core'
urlpatterns = [
    path('buscar', SearchTasksView.as_view(), name='search_tasks'),
    path('', HomeView.as_view(), name='home'),
]

