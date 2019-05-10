from django.contrib import admin
from film.models import Film, Rating, Director, Genre, Cast, Writer
# Register your models here.
admin.site.register(Film)
admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Writer)