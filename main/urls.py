# main/urls.py

from django.urls import path

from . import views


urlpatterns = [
    path(
        "api/<str:room_name>/",
        views.MessageAPIView.as_view(),
    ),
    path("", views.index, name="index"),
    path("<str:room_name>/<str:user_name>/", views.room, name="room"),
]
