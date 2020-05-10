from django.shortcuts import render
from rest_framework import viewsets, filters
from anime_list import serializers, models


class AnimeViewSet(viewsets.ModelViewSet):
    """API ViewSet for creating, viewing, updating anime"""
    serializer_class = serializers.AnimeSerializer
    queryset = models.Anime.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class AnimeSeasonViewSet(viewsets.ModelViewSet):
    """API ViewSet for managing seasons"""
    serializer_class = serializers.AnimeSeasonSerializer
    queryset = models.AnimeSeason.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_of_season')


class GenreViewSet(viewsets.ModelViewSet):
    """API ViewSet for managing genres"""
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()
