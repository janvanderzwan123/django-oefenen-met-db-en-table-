from . import views
from django.urls import path

urlpatterns = [
    path('table/', views.page, name='table'),
    path('search/', views.search_events, name='search_events'),
]