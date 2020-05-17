from django.test import TestCase
from .mock_values import *
from anime_list.models import Anime, Genre, AnimeSeason


class TestAnimeModel(TestCase):
    """Test cases for anime-list app"""

    def setUp(self):
        self.genre = Genre.objects.create_genre("test_genre")
        self.genre2 = Genre.objects.create(name="test_genre2")
        self.anime = Anime.objects.create_anime(
            "TESTANIME", "AUTHORTEST", [self.genre, self.genre2],
        )
        self.anime_season = AnimeSeason.objects.create(**get_mock_season(1, self.anime))

    def test_modal(self):
        self.assertEqual(self.anime.author, "AUTHORTEST")
        self.assertEqual(self.anime.name, "TESTANIME")

    def test_genres(self):
        genrelist = ["test_genre", "test_genre2"]
        self.assertEqual(self.anime.genre_names, genrelist)

    def test_season_count(self):
        mock_season_count = 0
        self.assertEqual(self.anime.season_count, 1)
        new_season = AnimeSeason.objects.create(**get_mock_season(2, self.anime))
        self.assertEqual(self.anime.season_count, 2)
