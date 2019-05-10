from django.db import models

# Create your models here.


class Director(models.Model):
    _id = models.CharField(max_length=20, verbose_name="编号", db_column="_id")
    name = models.CharField(
        max_length=500, verbose_name="姓名", db_column="name")

    class Meta:
        db_table = 'director'
        verbose_name_plural = '导演'
        verbose_name = 'director'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="genre", db_column="name")

    class Meta:
        db_table = 'genre'
        verbose_name_plural = '剧情'
        verbose_name = 'genre'

    def __str__(self):
        return self.name


class Cast(models.Model):
    _id = models.CharField(max_length=20, verbose_name="编号", db_column="_id")
    name = models.CharField(
        max_length=500, verbose_name="姓名", db_column="name")

    class Meta:
        db_table = 'cast'
        verbose_name_plural = '演员'
        verbose_name = 'cast'

    def __str__(self):
        return self.name


class Writer(models.Model):
    _id = models.CharField(max_length=20, verbose_name="编号", db_column="_id")
    name = models.CharField(
        max_length=500, verbose_name="姓名", db_column="name")

    class Meta:
        db_table = 'writer'
        verbose_name_plural = '编剧'
        verbose_name = 'writer'

    def __str__(self):
        return self.name


class Film(models.Model):
    _id = models.CharField(
        max_length=20, verbose_name="编号", db_column="_id", primary_key=True)
    season_count = models.CharField(
        max_length=100,
        verbose_name="季数",
        db_column="season_count",
        default=None)
    pubdate = models.CharField(
        max_length=500, verbose_name="发布时间", db_column="pubdate")
    countries = models.CharField(
        max_length=500, verbose_name="上映国家", db_column="countries")
    lens_id = models.IntegerField(
        verbose_name="L编号", db_column="lens_id", default=None)
    title = models.CharField(
        max_length=500, verbose_name="电影名", db_column="title")
    site = models.CharField(
        max_length=500, verbose_name="网站", db_column="site", default=None)
    poster = models.CharField(
        max_length=500, verbose_name="图片地址", db_column="poster")
    summary = models.CharField(
        max_length=3000, verbose_name="简介", db_column="summary")
    languages = models.CharField(
        max_length=500, verbose_name="语言", db_column="languages")
    episodes = models.CharField(
        max_length=100, verbose_name="集数", db_column="episodes", default=None)
    imdb = models.CharField(
        max_length=100, verbose_name="imdb编号", db_column="imdb")
    year = models.CharField(
        max_length=100, verbose_name="年份", db_column="year")
    duration = models.CharField(
        max_length=100, verbose_name="时长", db_column="duration")
    douban_site = models.CharField(
        max_length=200,
        verbose_name="豆瓣网址",
        db_column="douban_site",
        default=None)
    aka = models.CharField(
        max_length=600, verbose_name="别名", db_column="aka", default=None)
    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)
    casts = models.ManyToManyField(Cast)
    writers = models.ManyToManyField(Writer)

    class Meta:
        db_table = 'films'
        verbose_name_plural = '电影'
        verbose_name = 'films'

    def __str__(self):
        return self.title


class Rating(models.Model):
    film = models.OneToOneField(Film, on_delete=models.CASCADE)
    average = models.CharField(
        max_length=10, verbose_name="平均评分", db_column="average")
    rating_people = models.CharField(
        max_length=10, verbose_name="评分人数", db_column="rating_people")
    five = models.CharField(
        max_length=10, verbose_name="五星占比", db_column="five")
    four = models.CharField(
        max_length=10, verbose_name="四星占比", db_column="four")
    three = models.CharField(
        max_length=10, verbose_name="三星占比", db_column="three")
    two = models.CharField(max_length=10, verbose_name="二星占比", db_column="two")
    one = models.CharField(max_length=10, verbose_name="一星占比", db_column="one")

    class Meta:
        db_table = 'rating'
        verbose_name_plural = '评价'
        verbose_name = 'rating'

    def __str__(self):
        return self.film.title
