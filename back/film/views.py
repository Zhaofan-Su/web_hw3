from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from film.models import Director, Genre, Cast, Writer, Film, Rating
from film.serializers import DirectorSerializer, GenreSerializer, CastSerializer, WriterSerializer, FilmSerializer, RatingSerializer

# Create your views here.


@api_view(['GET'])
def detail(request, id):
    film = Film.objects.get(id=id)
    if film is None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = FilmSerializer(film)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
