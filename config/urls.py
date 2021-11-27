from django.urls import path, include

urlpatterns = [
    path("article", include("diary.urls")),
    path("user", include("user.urls")),
]
