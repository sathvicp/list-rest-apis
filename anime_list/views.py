from django.shortcuts import render
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from anime_list import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class AnimeViewSet(viewsets.ModelViewSet):
    """API ViewSet for creating, viewing, updating anime"""

    serializer_class = serializers.AnimeSerializer
    queryset = models.Anime.objects.all()
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    search_fields = ("name",)
    filterset_fields = (
        "no_of_seasons",
        "rating",
        "genre",
        "id",
    )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AdminCanEditPermission,)


class AnimeSeasonViewSet(viewsets.ModelViewSet):
    """API ViewSet for managing seasons"""

    serializer_class = serializers.AnimeSeasonSerializer
    queryset = models.AnimeSeason.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name_of_season",)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AdminCanEditPermission,)

    def create(self, request, *args, **kwargs):
        """Increment no_of_season for anime"""
        anime = models.Anime.objects.get(pk=request.data.get("anime"))
        anime.no_of_seasons = F("no_of_seasons") + 1
        anime.save(update_fields=["no_of_seasons"])
        return super().create(request, *args, **kwargs)


class GenreViewSet(viewsets.ModelViewSet):
    """API ViewSet for managing genres"""

    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AdminCanEditPermission,)
