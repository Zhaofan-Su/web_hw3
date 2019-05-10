from django.urls import path
from . import views

urlpatterns = [
    path('detail/<id>', views.detail),
    path('genre/<id>', views.get_films_by_genre),
    path('genres', views.get_all_genres),
    path('all', views.all),
    path('fuzzySearch/<opt>', views.search_films),
]
