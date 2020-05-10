from django.db import models
from hashlib import md5


class Genre(models.Model):
    """Model for Genres of anime"""
    name = models.CharField(max_length=30, primary_key=True)


class AnimeManager(models.Manager):
    """Manager for the Anime database model"""

    def create_anime(self, name, author, genres, no_of_seasons=None):
        anime = self.model(name=name, author=author,
                           no_of_seasons=no_of_seasons)
        anime.anime_id = md5(bytes(name, 'utf-8')).hexdigest()
        anime.save(using=self._db)
        return anime


class Anime(models.Model):
    """Model for details about an anime"""

    name = models.CharField(max_length=100)
    anime_id = models.CharField(max_length=32, primary_key=True)
    no_of_seasons = models.PositiveSmallIntegerField(default=1)
    author = models.CharField(max_length=40)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    genre = models.ManyToManyField(Genre, 'animes')

    objects = AnimeManager()

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
    name_of_season = models.CharField(max_length=100)
    no_of_episodes = models.IntegerField()
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'anime'
        get_latest_by = 'season'
        unique_together = ['anime', 'season']
