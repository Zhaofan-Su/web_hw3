from rest_framework.response import Response
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from film.models import Director, Genre, Cast, Writer, Film, Rating
from film.serializers import DirectorSerializer, GenreSerializer, CastSerializer, WriterSerializer, FilmSerializer, RatingSerializer
from django.db.models import Q
# Create your views here.


@api_view(['GET'])
def main(requset, pageNo):
    pageNo = int(pageNo)
    pageSize = 20
    films = Film.objects.all()
    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)

    start = (pageNo - 1) * pageSize
    end = len(films) if (start + pageSize >= len(films)) else start + pageSize

    serializer = FilmSerializer(films[start:end], many=True)
    context = {
        'films': serializer.data,
        'total': len(films),
    }
    return Response(data=context, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail(request, id):
    film = Film.objects.get(_id=id)
    if film is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = FilmSerializer(film)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_films_by_genre(request, id, pageNo):
    pageNo = int(pageNo)
    pageSize = 20
    genre = Genre.objects.get(id=id)
    films = genre.film_set.all()
    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)

    start = (pageNo - 1) * pageSize
    end = len(films) if (start + pageSize >= len(films)) else start + pageSize
    serializer = FilmSerializer(films[start:end], many=True)
    context = {
        'total': len(films),
        'films': serializer.data,
    }
    serializer = FilmSerializer(films, many=True)
    return Response(data=context, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_films(request, opt, pageNo):
    pageNo = int(pageNo)
    pageSize = 20
    films = []
    films.extend(
        Film.objects.filter(
            Q(title__exact=opt) | Q(title__icontains=opt)
            | Q(aka__icontains=opt)))
    for director in Director.objects.filter(
            Q(name__exact=opt) | Q(name__icontains=opt)):
        films.extend(director.film_set.all())

    if len(films) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)

    start = (pageNo - 1) * pageSize
    end = len(films) if (start + pageSize >= len(films)) else start + pageSize
    serializer = FilmSerializer(films[::-1][start:end], many=True)
    context = {
        'total': len(films),
        'films': serializer.data,
    }
    return Response(data=context, status=status.HTTP_200_OK)