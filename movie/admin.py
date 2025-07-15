from django.contrib import admin

from movie.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "duration")


admin.site.register(Movie, MovieAdmin)