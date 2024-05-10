from django.contrib import admin
from .models import Movie,genere

class GenereAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title','release_year','number_in_stock','daily_rate','genere','date_created')

admin.site.register(Movie,MovieAdmin)
admin.site.register(genere,GenereAdmin)

# Register your models here.
