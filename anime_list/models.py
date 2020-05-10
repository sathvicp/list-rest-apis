from django.db import models
from hashlib import md5


class GenreManager(models.Manager):
    """Manager for managing the genres in meta"""

    def create_genre(self, name: str):
        genre = self.model(name=name)
        genre.save(using=self._db)
        return genre


class Genre(models.Model):
    """Model for Genres of anime"""
    name = models.CharField(max_length=30, unique=True)

    objects = GenreManager()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class AnimeManager(models.Manager):
    """Manager for the Anime database model"""

    def create_anime(self, name, author, genres: list = []):
        anime = self.model(name=name, author=author)
        anime.save(using=self._db)
        for genre in genres:
            anime.genre.add(genre)
        return anime


class Anime(models.Model):
    """Model for details about an anime"""

    name = models.CharField(max_length=100)
    no_of_seasons = models.PositiveSmallIntegerField(default=0)
    author = models.CharField(max_length=40)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    no_of_ratings = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre, 'animes')

    objects = AnimeManager()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


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
    airing = models.BooleanField()
    time_of_year = models.CharField(max_length=3, choices=TIME_OF_YEAR_CHOICES)
    year = models.PositiveSmallIntegerField()
    name_of_season = models.CharField(max_length=100)
    no_of_episodes = models.PositiveSmallIntegerField()
    anime = models.ForeignKey(
        Anime, related_name='seasong', on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'anime'
        get_latest_by = 'season'
        unique_together = ['anime', 'season']
