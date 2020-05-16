from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

doc_schema = get_schema_view(
    openapi.Info(
        title="Stampede web APIs",
        default_version="v1",
        description="Documentation of REST APIs",
        terms_of_service="no",
        contact=openapi.Contact(name="Sathvic", email="sathvic.p@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("anime-list/", include("anime_list.urls")),
    path("profile/", include("profiles.urls")),
    path(
        "doc/", doc_schema.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("redoc/", doc_schema.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
