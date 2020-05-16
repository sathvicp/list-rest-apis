from django.urls import path, include

from rest_framework.routers import DefaultRouter

from anime_list import views

router = DefaultRouter()
router.register("anime", views.AnimeViewSet)
router.register("season", views.AnimeSeasonViewSet)
router.register("genre", views.GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
