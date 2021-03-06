# Generated by Django 2.2.1 on 2019-05-10 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_column='_id', max_length=20, verbose_name='编号')),
                ('name', models.CharField(db_column='name', max_length=500, verbose_name='姓名')),
            ],
            options={
                'verbose_name': 'cast',
                'verbose_name_plural': '演员',
                'db_table': 'cast',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_column='_id', max_length=20, verbose_name='编号')),
                ('name', models.CharField(db_column='name', max_length=500, verbose_name='姓名')),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': '导演',
                'db_table': 'director',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('_id', models.CharField(db_column='_id', max_length=20, primary_key=True, serialize=False, verbose_name='编号')),
                ('season_count', models.CharField(db_column='season_count', default=None, max_length=100, verbose_name='季数')),
                ('pubdate', models.CharField(db_column='pubdate', max_length=500, verbose_name='发布时间')),
                ('countries', models.CharField(db_column='countries', max_length=500, verbose_name='上映国家')),
                ('lens_id', models.IntegerField(db_column='lens_id', default=None, verbose_name='L编号')),
                ('title', models.CharField(db_column='title', max_length=500, verbose_name='电影名')),
                ('site', models.CharField(db_column='site', default=None, max_length=500, verbose_name='网站')),
                ('poster', models.CharField(db_column='poster', max_length=500, verbose_name='图片地址')),
                ('summary', models.CharField(db_column='summary', max_length=3000, verbose_name='简介')),
                ('languages', models.CharField(db_column='languages', max_length=500, verbose_name='语言')),
                ('episodes', models.CharField(db_column='episodes', default=None, max_length=100, verbose_name='集数')),
                ('imdb', models.CharField(db_column='imdb', max_length=100, verbose_name='imdb编号')),
                ('year', models.CharField(db_column='year', max_length=100, verbose_name='年份')),
                ('duration', models.CharField(db_column='duration', max_length=100, verbose_name='时长')),
                ('douban_site', models.CharField(db_column='douban_site', default=None, max_length=200, verbose_name='豆瓣网址')),
                ('aka', models.CharField(db_column='aka', default=None, max_length=600, verbose_name='别名')),
                ('casts', models.ManyToManyField(to='film.Cast')),
                ('directors', models.ManyToManyField(to='film.Director')),
            ],
            options={
                'verbose_name': 'films',
                'verbose_name_plural': '电影',
                'db_table': 'films',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='genre')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': '剧情',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_column='_id', max_length=20, verbose_name='编号')),
                ('name', models.CharField(db_column='name', max_length=500, verbose_name='姓名')),
            ],
            options={
                'verbose_name': 'writer',
                'verbose_name_plural': '编剧',
                'db_table': 'writer',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.CharField(db_column='average', max_length=10, verbose_name='平均评分')),
                ('rating_people', models.CharField(db_column='rating_people', max_length=10, verbose_name='评分人数')),
                ('five', models.CharField(db_column='five', max_length=10, verbose_name='五星占比')),
                ('four', models.CharField(db_column='four', max_length=10, verbose_name='四星占比')),
                ('three', models.CharField(db_column='three', max_length=10, verbose_name='三星占比')),
                ('two', models.CharField(db_column='two', max_length=10, verbose_name='二星占比')),
                ('one', models.CharField(db_column='one', max_length=10, verbose_name='一星占比')),
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='film.Film')),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': '评价',
                'db_table': 'rating',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(to='film.Genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='writers',
            field=models.ManyToManyField(to='film.Writer'),
        ),
    ]
