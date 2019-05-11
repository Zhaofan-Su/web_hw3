from django.urls import path
from . import views

urlpatterns = [
    path('detail/<id>', views.detail),
    path('genre/<id>/<pageNo>', views.get_films_by_genre),
    path('genres', views.get_all_genres),
    path('main/<pageNo>', views.main),
    path('fuzzySearch/<opt>/<pageNo>', views.search_films),
]
