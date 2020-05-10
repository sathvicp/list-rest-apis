from django.urls import path, include

urlpatterns = [
    path('anime-list/', include('anime_list.urls'))
]
