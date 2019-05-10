from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from film.models import Director, Genre, Cast, Writer, Film, Rating
from film.serializers import DirectorSerializer, GenreSerializer, CastSerializer, WriterSerializer, FilmSerializer, RatingSerializer
from django.db.models import Q
# Create your views here.


@api_view(['GET'])
def all(requset):
    films = Film.objects.all()[:100]
    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = FilmSerializer(films, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail(request, id):
    film = Film.objects.get(_id=id)
    if film is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = FilmSerializer(film)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_films_by_genre(request, id):
    genre = Genre.objects.get(id=id)
    films = genre.film_set.all()[:100]
    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = FilmSerializer(films, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_films(request, opt):
    films = []
    films.extend(
        Film.objects.filter(Q(title__icontains=opt) | Q(aka__icontains=opt)))
    for director in Director.objects.filter(name__icontains=opt):
        films.extend(director.film_set.all())

    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = FilmSerializer(films[0:2], many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)