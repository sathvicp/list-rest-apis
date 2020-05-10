from django.db import models


class Anime(models.Model):
    """Model for details about an anime"""

    name = models.CharField()
    anime_id = models.CharField(max_length=32, min_length=32, primary_key=True)
    no_of_seasons = models.PositiveSmallIntegerField(default=1)
    author = models.CharField(max_length=40)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    genre = models.ManyToManyField(Genre, 'animes')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class AnimeSeason(models.Model):
    """Model for different seasons of an anime"""
    WINTER = 'WIN'
    SPRING = 'SPR'
    SUMMER = 'SUM'
    FALL = 'FAL'
    TIME_OF_YEAR_CHOICES = [
        (WINTER, 'Winter'),
        (SPRING, 'Sprint'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
    ]
    season = models.PositiveSmallIntegerField()
    time_of_year = models.CharField(max_length=3, choices=TIME_OF_YEAR_CHOICES)
    year = models.PositiveSmallIntegerField()
    name_of_season = models.CharField()
    no_of_episodes = models.IntegerField()
    anime = models.ForeignKey('AnimeModel', on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'anime'
        get_latest_by = 'season'
        unique_together = ['anime', 'season']


class Genre(models.Model):
    """Model for Genres of anime"""
    name = models.CharField(primary_key=True)
