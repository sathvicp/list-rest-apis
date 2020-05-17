from rest_framework import serializers
from anime_list import models


class GenreSerializer(serializers.ModelSerializer):
    """Serializes genres"""

    class Meta:
        model = models.Genre
        fields = ("name",)

    def create(self, validated_data):
        """Create a genre entry in meta"""
        genre = models.Genre.objects.create_genre(name=validated_data["name"])
        return genre


class GenreField(serializers.StringRelatedField):
    """Genre field"""

    def to_internal_value(self, value):
        genre = models.Genre.objects.filter(name=value.lower())
        if genre and len(genre) == 1:
            return genre.get().id
        else:
            raise serializers.ValidationError(f'Genre with name "{value}" not found')


class AnimeSerializer(serializers.ModelSerializer):
    """Serializes an anime object"""

    genre = GenreField(many=True,)

    class Meta:
        model = models.Anime
        fields = (
            "name",
            "season_count",
            "author",
            "rating",
            "genre",
            "id",
        )
        extra_kwargs = {
            "rating": {"read_only": True,},
            "id": {"read_only": True,},
        }

    def create(self, validated_data):
        """Create an anime entry in meta"""
        anime = models.Anime.objects.create_anime(
            name=validated_data["name"],
            author=validated_data["author"],
            genres=validated_data["genre"],
        )
        return anime


class AnimeSeasonSerializer(serializers.ModelSerializer):
    """Serializes anime seasons"""

    class Meta:
        model = models.AnimeSeason
        fields = (
            "season",
            "airing",
            "time_of_year",
            "year",
            "name_of_season",
            "anime",
            "episode_count",
        )
