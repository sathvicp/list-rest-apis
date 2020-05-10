from django.contrib import admin
from anime_list import models

# Register your models here.

admin.site.register(models.Anime)
admin.site.register(models.AnimeSeason)
admin.site.register(models.Genre)