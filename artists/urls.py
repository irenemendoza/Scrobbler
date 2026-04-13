from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_search, name='artist_search'),
    path('api/artist/', views.artist_search_api, name='artist_search_api'),
]