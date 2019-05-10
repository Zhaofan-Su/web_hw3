import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_hw3.settings')

import django
django.setup()

from film.models import Rating, Director, Genre, Cast, Writer, Film


# 载入数据
def get_data():
    with open('films_all.json', 'rb') as f:
        # 解析每一行数据
        datas = json.load(f)
    return datas


def clear():
    Rating.objects.all().delete()
    Director.objects.all().delete()
    Genre.objects.all().delete()
    Cast.objects.all().delete()
    Writer.objects.all().delete()
    Film.objects.all().delete()


def data_dump(datas):

    # directors_query =[]
    # genres_query =[]
    # casts_query=[]
    # writers_query = []
    # films_query=[]
    # ratings_query=[]

    i = 0
    for data in datas:
        i += 1
        print(i)
        directors = set()
        for director_raw in data['directors']:
            director, _ = Director.objects.get_or_create(
                _id=director_raw['id'], name=director_raw['name'])
            # if director not in directors_query:
            #     directors_query.append(director)
            directors.add(director)
            # 也许会出错？
            # director.save()

        genres = set()
        for genre_raw in data['genres']:
            genre, _ = Genre.objects.get_or_create(name=genre_raw)
            # if genre not in genres_query:
            #     genres_query.append(genre)
            genres.add(genre)
            # genre.save()

        casts = set()
        for cast_raw in data['casts']:
            cast, _ = Cast.objects.get_or_create(
                _id=cast_raw['id'], name=cast_raw['name'])
            # if cast not in casts_query:
            #     casts_query.append(cast)
            casts.add(cast)
            # cast.save()

        writers = set()
        for writer_raw in data['writers']:
            writer, _ = Writer.objects.get_or_create(
                _id=writer_raw['id'], name=writer_raw['name'])
            # if writer not in writers_query:
            #     writers_query.append(writer)
            writers.add(writer)
            # writer.save()

        countries = ''
        for country in data['countries']:
            countries += country + ","

        languages = ''
        for language in data['languages']:
            languages += language + ","

        akas = ''
        for aka in data['aka']:
            akas += aka + ","

        film, _ = Film.objects.get_or_create(
            _id=data['_id'],
            season_count=data['season_count'],
            pubdate=data['pubdate'],
            countries=countries[:-1],
            lens_id=data['lens_id'],
            title=data['title'],
            site=data['site'],
            poster=data['poster'],
            summary=data['summary'],
            languages=languages[:-1],
            episodes=data['episodes'],
            imdb=data['imdb'],
            year=data['year'],
            duration=data['duration'],
            douban_site=data['douban_site'],
            aka=akas[:-1])
        film.directors.set(directors)
        film.genres.set(genres)
        film.casts.set(casts)
        film.writers.set(writers)

        # films_query.append(film)

        if len(data['rating']['stars']) == 0:
            rating = Rating.objects.create(
                film=film,
                average=data['rating']['average'],
                rating_people=data['rating']['rating_people'],
                five='',
                four='',
                three='',
                two='',
                one='')
            # ratings_query.append(rating)
        else:
            rating = Rating.objects.create(
                film=film,
                average=data['rating']['average'],
                rating_people=data['rating']['rating_people'],
                five=data['rating']['stars'][0],
                four=data['rating']['stars'][1],
                three=data['rating']['stars'][2],
                two=data['rating']['stars'][3],
                one=data['rating']['stars'][4])
            # ratings_query.append(rating)
        # rating.save()

    # Director.objects.bulk_create(directors_query)
    # Genre.objects.bulk_create(genres_query)
    # Cast.objects.bulk_create(casts_query)
    # Writer.objects.bulk_create(writers_query)
    # Film.objects.bulk_create(films_query)
    # Rating.objects.bulk_create(ratings_query)


if __name__ == "__main__":
    films = get_data()
    # data_dump(films)
    data_dump(films[10000:])
    # data_dump(films[10000:])
    # clear()
    # print(type(films[0]['rating']['stars'][4]))
    print("done")