from rest_framework import serializers
from film.models import Film, Rating, Director, Genre, Cast, Writer


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("_id", "name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ("_id", "name")


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ("_id", "name")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("average", "rating_people", "five", "four", "three", "two",
                  "one")


class FilmSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True)
    genres = GenreSerializer(many=True)
    casts = CastSerializer(many=True)
    writers = WriterSerializer(many=True)
    rating = RatingSerializer()

    class Meta:
        model = Film
        fields = ("_id", "season_count", "pubdate", "countries", "lens_id",
                  "title", "site", "poster", "summary", "languages",
                  "episodes", "imdb", "year", "duration", "douban_site", "aka",
                  "directors", "genres", "casts", "writers", "rating")
